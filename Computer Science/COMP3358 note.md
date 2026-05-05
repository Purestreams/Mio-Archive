---
geometry: margin=1.5cm
---

# COMP3358 Revision Note

### Part 1: Comprehensive Revision Notes

#### 1. Distributed Systems & Middleware Architecture
*   **The TCP/IP Protocol Stack:** Operates natively over Transport (TCP, UDP), Network (IP), and Data Link (Ethernet) layers, utilizing the Sockets API (`connect()`, `listen()`) as the fundamental network programming interface.
*   **Web Services & Messaging Paradigms:**
    *   **SOAP & WSDL:** SOAP uses XML for transport over HTTP/SMTP/UDP, while WSDL uses XML to describe the service's technical details (methods, port types, endpoints).
    *   **UDDI:** Acts as the registry/directory for client applications to discover these web services.
    *   **JMS (Java Message Service):** Supports **Synchronous** messaging (client blocks and waits for a reply, like a phone call) and **Asynchronous** messaging (event-triggered, no waiting, like an email).
*   **Remote Procedure Call (RPC) Deep Dive:** 
    *   Standard RPC execution follows 6 strict steps: The client calls the local stub -> Stub marshals parameters into a network message -> OS transmits packet -> Server OS receives packet -> Server skeleton unmarshals parameters -> Server procedure is invoked.
    *   **Standard vs. Multi-threaded:** Standard RPC blocks the client and server processes entirely. Multi-threaded RPC allows servers to handle thousands of concurrent clients and clients to remain responsive, but introduces severe shared-state synchronization hazards (requiring locks).
*   **Java RMI (Remote Method Invocation) Advanced Mechanics:**
    *   **The Stub:** Acts as the client's local proxy. It initiates the JVM connection, marshals parameters, waits, and unmarshals the return value.
    *   **UnicastRemoteObject:** The base class for standard transient point-to-point servers. It automatically exports the object to the RMI runtime and listens on a TCP port upon construction.
    *   **Object Serialization:** To be transmitted over RMI, a class *and all of its member fields* must strictly implement `java.io.Serializable`.
    *   **Dynamic Class Loading & Polymorphism:** RMI supports fetching missing stub class definitions from remote HTTP/FTP servers at runtime (via `java.rmi.server.codebase`). This enables remote polymorphism, where a client can receive and execute a concrete subclass (e.g., an `MP3` object) even if it only asked for the base class (`Multimedia`).

#### 2. Transactions, ACID, and Two-Phase Commit (2PC)
*   **ACID Properties & Common Violations:**
    *   **Atomicity:** All-or-nothing execution. Violated if a transaction is partially completed and then overwritten by another concurrent transaction.
    *   **Consistency:** Data transforms from one valid state to another. Violated if two concurrent operations update the same variable and one update is lost.
    *   **Isolation:** Transactions must remain hidden from each other. Violated if variables are read *outside* of a locked critical section, or if a lock is released and re-acquired mid-transaction, allowing other transactions to sneak in and modify the state.
    *   **Durability:** Committed data is saved permanently and survives crashes.
*   **Two-Phase Commit (2PC) Mechanics & Failure Edge Cases:**
    *   **Purpose:** Ensures all-or-nothing atomicity across distributed nodes.
    *   **Phase 1 (Prepare):** Participants lock resources, write to a persistent log, and vote 'Yes' or 'No'. 
    *   **Phase 2 (Commit/Abort):** Coordinator evaluates votes. A single 'No' or a timeout forces a global abort.
    *   **The Availability Trade-off:** 2PC is fundamentally unsuited for high availability; if even one replica server crashes, 2PC will abort every write, taking the system offline.
    *   **Coordinator Crashes:** If a coordinator crashes *after* deciding to commit but before telling all participants, it must recover this decision from its persistent storage upon reboot and resend the COMMIT messages.
    *   **Split-Brain Danger:** If a client assumes a dead coordinator is gone and restarts the transaction with a *new* coordinator (who decides to abort), but the *old* coordinator wakes up and sends its previous commit messages, atomicity is fatally violated.

#### 3. Concurrency, Locks, and Consistency Models
*   **Scalability & Amdahl's Law:** Parallel scalability is strictly bounded by the non-parallelizable (serial) fraction of the workload. Coarse-grain parallelism (large independent tasks) is highly efficient, whereas fine-grain parallelism wastes runtime on communication overhead.
*   **Sequential Consistency (SC):**
    *   Requires a single global execution order that all processes agree upon.
    *   *Reachability Rule:* If all processors read old initial values (e.g., A, B, C = 0) after their respective writes, it is mathematically impossible under SC because it creates an unresolvable chronological cycle.
*   **Causal Consistency:** Weaker than SC. Enforces identical global ordering *only* for causally linked events (e.g., if P1 writes a value, and P2 reads that value and writes a new one, all nodes must see P1's write before P2's write). Independent concurrent writes can be seen in any order.
*   **Strict Locking Rules:**
    *   **Read-Only Transactions:** Someone claiming read-only transactions don't need locks is **wrong**. Without locks, a read-only transaction can observe a non-serializable, intermediate state (e.g., seeing one variable updated but not another).
    *   **Early Lock Release:** Releasing a lock immediately after using a variable (before the transaction ends) is **unsafe** and breaks two-phase locking, leading to non-serializable outcomes.

#### 4. Distributed Consensus: Raft & Blockchains
*   **Raft Protocol Mechanics:**
    *   **Log Configuration Rules:** Log terms must strictly be non-decreasing as the index increases (e.g., term 3 cannot precede term 2). Furthermore, a log cannot contain "holes"; missing entries are illegal.
    *   **Commit Safety:** Log entries are only "safe to apply" to state machines if they are present on a majority of nodes *and* are protected from being overwritten by any potential future leader.
    *   **Old Leader Edge Case:** An old, disconnected leader can actually finish committing an old log entry if it receives delayed AppendEntries responses from a majority that overlaps with the new leader's majority. This doesn't break Raft because the new leader is forced to preserve that committed entry.
*   **PBFT (Practical Byzantine Fault Tolerance):** Tolerates up to $f$ malicious nodes using a minimum of $3f+1$ total nodes. BFT provides absolute mathematical safety, but only best-effort liveness.
*   **Enterprise Blockchains:**
    *   **Hyperledger Fabric (HLF):** Uses an "Execute-Order-Validate" workflow. Endorsing peers execute logic before ordering. It supports non-deterministic logic but throughput collapses under high contention.
    *   **BIDL:** A datacenter-optimized architecture that runs Execution and Consensus phases in *parallel* concurrently, achieving low latency, high contention throughput, and non-deterministic support.

#### 5. Large-Scale Data Processing: MapReduce & Spark
*   **MapReduce Design Constraints:**
    *   **Strict Statelessness:** `map` and `reduce` functions must never use static or persisted variables (like `HashMap`s) to track state between records, because the framework does not guarantee execution order or worker assignment.
    *   **No Manual I/O:** Developers must never perform manual file reading/writing inside the functions; all output must use the `emit()` method.
    *   **Key Overloading:** Mapping all records to a single intermediate key destroys parallelism and causes job failure.
*   **Apache Spark Advantages:**
    *   **In-Memory RDDs:** By caching Resilient Distributed Datasets in memory, Spark avoids the catastrophic disk I/O overhead of Hadoop, achieving sorting records 3x faster with 1/10th the nodes.
    *   **Transformations vs. Actions:** Transformations (e.g., `map`, `filter`) are lazily evaluated and create new RDDs. Actions (e.g., `collect`, `count`) trigger actual execution. 
    *   **Narrow vs. Wide:** Narrow transformations (like `map`) execute locally. Wide transformations (like `groupByKey`) require an expensive cross-cluster network shuffle.
*   **Spark Streaming:** Operates on Discretized Streams (DStreams) by breaking live data into micro-batches (as small as 0.5 seconds). It provides exactly-once processing and can recover from node failures in less than 1 second.

#### 6. Production Traffic & Caching (Facebook Photo Stack)
*   **Traffic Distribution:** The client browser cache is the hero of the stack, absorbing 65.5% of all traffic. The Edge PoP absorbs 20%, the Origin Cache 4.6%, leaving the Haystack Backend to serve only 9.9% of total traffic.
*   **The Backend's Role:** While the edge caches serve viral "head" content, the backend storage effectively serves the vast "tail" of the popularity distribution (highly unpopular, rarely accessed photos).
*   **S4LRU Segmented Caching:** S4LRU splits the cache into 4 tiers (L3 down to L0). New misses are safely quarantined in the lowest L0 segment and are only promoted to higher segments upon proven reuse. S4LRU at 1/3 the memory footprint matches standard FIFO performance.

---

### Part 2: Core Mathematical Formulas & Physical Intuition

#### 1. Speedup Ratio
$$S_N = \frac{T_1}{T_n}$$
*   **$S_N$**: Speedup achieved on $N$ parallel cores (Unitless ratio)
*   **$T_1$**: Total completion time running on a single core (Seconds / Time unit)
*   **$T_n$**: Total completion time running on $n$ parallel cores (Seconds / Time unit)

**Physical Explanation:**
This formula measures the tangible real-world benefit of parallel computing. It quantifies how much faster a task completes when spreading the workload across multiple processors compared to doing it entirely alone on one processor. Ideally, $n$ processors would yield an $n$-times speedup, but coordination overhead always makes this sub-linear in reality.

#### 2. Amdahl's Law
$$S_{overall} = \frac{1}{(1-f) + \frac{f}{S_{part}}}$$
*   **$S_{overall}$**: Total theoretical maximum system speedup (Unitless ratio)
*   **$f$** (or **$B$**): The fraction of the algorithm that can be parallelized (Percentage / Decimal, e.g., 0.99)
*   **$S_{part}$** (or **$n$**): The speedup achieved for the parallelizable portion, often represented by the number of cores (Integer / Unitless ratio)

**Physical Explanation:**
Amdahl's Law acts as the universal speed limit for distributed systems. It mathematically proves that you cannot parallelize your way out of a sequential bottleneck. Even if you have an infinite number of processors, the time it takes to run the strictly sequential portion of your code (the $1-f$ portion) will act as a permanent ceiling on your overall performance.

#### 3. Distributed Garbage Collection (DGC) Reference Counting
$$RC = RC + 1$$
$$RC = RC - 1$$
$$RC = 0$$
*   **$RC$**: Reference Counter (Integer / Count)

**Physical Explanation:**
This is the life-support monitor for remote objects in Java RMI. Because servers cannot instantly know if a remote client has crashed or disconnected, they maintain a counter. Whenever a client across the network requests access to an object, the counter increments. When they release it, it decrements. The physical rule is simple: the moment $RC$ drops to zero, the object is completely orphaned on the network, and the server safely deletes it to free up memory.

#### 4. Deterministic Consistent Object Routing
$$\text{Assigned Origin Cache} = \text{Hash}(\text{url})$$
*   **$\text{Assigned Origin Cache}$**: The specific physical backend server assigned to hold the data (Identifier)
*   **$\text{url}$**: The specific resource being requested (String identifier)
*   **$\text{Hash}$**: A consistent hashing function (Algorithmic function)

**Physical Explanation:**
In a massive system like Facebook's photo cache, you cannot afford to query every server to ask "Do you have this photo?". This equation acts as a deterministic map. By passing the photo's URL through a fixed mathematical hash, every edge router in the world independently calculates the exact same target origin server. This guarantees only one global cached copy of the object exists at the origin tier, preventing data duplication.

#### 5. BFT Node Constraint and Quorum Safety
$$(N-f) + (N-f) - N \ge f+1 \implies N \ge 3f+1$$
*   **$N$**: Total number of consensus nodes in the cluster (Integer)
*   **$f$**: Maximum number of tolerated Byzantine (malicious or failed) nodes (Integer)

**Physical Explanation:**
This inequality defines the exact threshold of trust required to prevent a network "split-brain" under attack by malicious actors. In a BFT system, an operation is confirmed when a quorum of $N-f$ nodes agrees. The physics of the system dictate that to prevent a malicious actor from confirming two conflicting truths simultaneously, any two quorums *must* physically overlap by at least one verifiably honest node ($f+1$). Solving this geometric overlap requirement reveals that the cluster must contain a minimum of $3f+1$ total nodes to safely neutralize $f$ traitors.

## Additional Question

I would be happy to help you further prepare for the COMP3358 exam. Based strictly on the provided lecture notes and past paper structures, I have generated two additional sets of practice questions. 

These questions mirror the format of the sample exams and test your understanding of core distributed computing concepts, mathematical formulas, and system behaviors.

---

### Practice Exam Set A

**Question 1. Basic Concepts**
*(Each answer should contain no more than 50 English words).*

**(a) What is marshalling in Remote Procedure Calls (RPC)?**

**Answer:** Marshalling is the standardisation process of packing procedure parameters into a formatted network message for transport. It resolves cross-system incompatibilities, including architecture differences like byte order (endianness), numeric type sizing, and character encoding.

**(b) In Java RMI, what is the purpose of the Remote Reference Layer?**

**Answer:** The Remote Reference Layer is responsible for serializing request objects for network transmission. It also resolves invocation semantics, such as determining if a target object can be auto-started, before passing the prepared request data down to the Transport Layer.

**(c) What is the fundamental difference between strong consistency and eventual consistency?**

**Answer:** Under strong consistency, once an update completes, all subsequent accesses from any client are guaranteed to return the updated value. Eventual consistency is weaker; if no further updates are made, reads will only *eventually* return the most recent value.

---

**Question 2. Amdahl's Law**
Assume 5% of the runtime of a program is strictly serial and cannot be parallelized. This program is executed on a cluster utilizing 20 cores. Assuming the program runs at the same speed on all cores and there are no coordination overheads, what is the parallel speedup? 

**Answer:**
Amdahl's law defines the maximum theoretical speedup of a parallelized system. The formula for overall speedup is:
$$S_{overall} = \frac{1}{(1-f) + \frac{f}{S_{part}}}$$
*   The serial fraction $f$ (or $B$) = 0.05.
*   The parallel fraction is 0.95.
*   The number of cores $S_{part}$ (or $n$) = 20.

$$S_{overall} = \frac{1}{0.05 + \frac{0.95}{20}}$$
$$S_{overall} = \frac{1}{0.05 + 0.0475}$$
$$S_{overall} = \frac{1}{0.0975}$$
$S_{overall} \approx 10.25$
The parallel speedup for the program is approximately **10.25**.

---

**Question 3. Raft Consensus Protocol**
Suppose a Raft follower's election timeout expires because it has not received any valid RPCs (heartbeats) from the current leader. 
Describe the exact sequence of four actions this server must take immediately upon transitioning to the Candidate state.

**Answer:** 
Upon entering the Candidate state, the server must sequentially:
1. Increment its local `currentTerm` value.
2. Cast an election vote for itself.
3. Reset its election timeout.
4. Broadcast `RequestVote` RPCs to all other servers in the cluster to gather a majority.

---

**Question 4. MapReduce Framework**
A developer writes a MapReduce program and decides to map *all* input records to the exact same intermediate key (e.g., `emit("FOO", value)`). Explain why this is a critical design mistake.

**Answer:**
Mapping all input records to a single intermediate key overloads the single reduce worker assigned to that specific key. This completely eliminates all parallelism in the reduce phase, creating a massive bottleneck that will almost always cause the job to fail. MapReduce relies on distributing different intermediate keys across multiple reducers to achieve horizontal scalability.

---

### Practice Exam Set B

**Question 1. Two-Phase Commit (2PC) & Failures**
In a distributed transaction utilizing the 2PC protocol, Coordinator B sends a "prepare" check to participants Node A and Node C. Node A successfully persists its state and responds with a `Yes` vote. However, Node C crashes and fails to respond before the timeout.

**(a) What is the coordinator's final global decision?**

**Answer:** The coordinator will broadcast an `Abort` decision. In 2PC, a commit is only issued if *every single participant* votes `Yes`; if any participant fails to respond or times out, it is treated as a `No`, triggering a global abort.

**(b) What must Node A do with its acquired locks and pending state while waiting for the coordinator's final decision?**

**Answer:** After voting `Yes` and entering the "prepared to commit" state, Node A must block indefinitely and cannot resolve the transaction until it learns the official outcome. It must retain all pending transaction updates and hold all locks acquired for this transaction; nothing can be released.

---

**Question 2. Consistency Models**
Consider the following execution trace for a shared variable `x` across three processors. Time flows from left to right.
*   **P1:** `W(x)1`
*   **P2:** `R(x)1` -> `W(x)2`
*   **P3:** `R(x)2` -> `R(x)1`

**Is this execution valid under Causal Consistency? Explain why or why not.**

**Answer:**
No, this trace is invalid under Causal Consistency. 
Because P2 observed the value `1` before issuing its write for `2`, an explicit causal relationship is established: `W(x)1` is causally ordered *before* `W(x)2`. Causal consistency mandates that all clients must observe causally linked writes in their correct original order. P3 violates this global ordering rule by reading the older value `1` *after* it has already observed the newer value `2`.

---

**Question 3. Distributed Deadlocks**
Two concurrent transactions are executing. Transaction 1 attempts to transfer $100 from Account Alice to Account Bob. Transaction 2 attempts to transfer $500 from Account Bob to Account Alice. Both use locking to enforce mutual exclusion.

**Outline the exact interleaved sequence of lock operations that leads to a deadlock.**

**Answer:**
A deadlock occurs when neither processor can make progress because they are indefinitely waiting for locks held by each other. The sequence is:
1. Transaction 1 successfully executes `LOCK(Bob)`.
2. Transaction 2 successfully executes `LOCK(Alice)`.
3. Transaction 1 attempts to execute `LOCK(Alice)` but blocks because Transaction 2 currently holds it.
4. Transaction 2 attempts to execute `LOCK(Bob)` but blocks because Transaction 1 currently holds it.

---

**Question 4. Workload Analysis & Caching (Facebook Photo Stack)**
When evaluating the Facebook photo cache workload, two sampling methods were considered: Request-based sampling and Object-based sampling.

**(a) Why does Request-based sampling produce inaccurate measurements for this specific workload?**

**Answer:** Request-based sampling captures a fixed percentage of all incoming requests. Because photo requests follow a power-law distribution, this method introduces a strong bias towards highly popular content and artificially inflates the measured cache performance, providing zero coverage for the long tail of unpopular content.

**(b) Which caching algorithm provided the highest hit ratio for the edge cache, and how does it handle new cache misses?**

**Answer:** The **S4LRU** (Segmented 4-level LRU) cache provided the highest hit ratio. When a cache miss occurs, S4LRU never places new objects directly into higher tiers; new missed objects are inserted exclusively into the lowest priority `L0` segment.