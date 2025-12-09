# Java OOP Exam Revision Notes

## 1. The Four Pillars of OOP
* **Encapsulation:** Hiding internal state and requiring interaction through methods (e.g., `private` fields with public getters/setters).
* **Inheritance:** Acquiring properties and methods from a parent class using `extends`.
* **Polymorphism:**
    * *Subtype Polymorphism:* Using a superclass reference to hold a subclass object (e.g., `Shape s = new Circle();`).
    * *Method Overriding:* A subclass provides a specific implementation of a method defined in the superclass.
* **Abstraction:** Hiding complex implementation details and exposing only the necessary features (via `abstract` classes or `interface`s).

---

## 2. Inheritance Mechanics
### Overloading vs. Overriding
* **Overloading (Compile-time):**
    * Same method name.
    * **Different** parameter list (type or number of arguments).
    * Return type alone does not distinguish overloaded methods.
* **Overriding (Runtime):**
    * Same method name.
    * **Same** parameter list.
    * Occurs in a subclass.
    * Use `@Override` annotation to prevent errors.

### Abstract Class vs. Interface
| Feature | Abstract Class | Interface |
| :--- | :--- | :--- |
| **Instantiation** | Cannot be instantiated. | Cannot be instantiated. |
| **Constructors** | **Yes** (invoked by subclasses). | **No**. |
| **Methods** | Can have abstract and concrete methods. | Only abstract (mostly) methods. |
| **State** | Can have instance variables (state). | Constants (`static final`) only. |
| **Usage** | "Is-a" relationship (shared identity). | "Can-do" relationship (capability). |
| **Inheritance** | A class extends **one** class. | A class implements **multiple** interfaces. |

### Constructor Chaining
* When a subclass object is created, the **superclass constructor** is always called first.
* If you don't call `super()` explicitly, Java calls the no-arg `super()` automatically.
* **Exam Trap:** If `SchoolBus extends Bus extends Vehicle`, creating a `SchoolBus` invokes 3 constructors (Vehicle -> Bus -> SchoolBus).

---

## 3. Memory Management
* **Heap:** All **Objects** live here.
* **Stack:** Local variables (primitives and object references) and method calls live here.
* **Garbage Collection:** An object is eligible for GC when there are **no active references** to it (e.g., reference set to `null`).
* **Object Counting:**
    * `String s = "A";` (String pool, might reuse).
    * `String s = new String("A");` (Force new object).
    * `Long x = (long)1;` (Autoboxing creates a wrapper object).

---

## 4. Exception Handling
* **Checked Exceptions:**
    * Checked at compile-time.
    * Must be handled (`try-catch`) or declared (`throws`).
    * *Examples:* `IOException`, `FileNotFoundException`, `ClassNotFoundException`.
* **Unchecked (Runtime) Exceptions:**
    * Result of programming logic errors.
    * Not required to catch.
    * *Examples:* `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`.
* **The `finally` block:**
    * Always executes (success or failure), usually for cleanup (closing streams).

---

## 5. GUI Programming (AWT & Swing)
* **Layout Managers:**
    * `BorderLayout`: North, South, East, West, Center.
    * `GridLayout`: Rows and Columns (fills left-to-right, top-to-bottom).
* **Key Methods to Memorize:**
    * `public void paintComponent(Graphics g)`: Override this in a `JPanel` to draw.
    * `super.paintComponent(g)`: **Always** call this first to clear the screen.
    * `repaint()`: Call this to trigger a screen update after changing data.
    * `g.drawOval(x, y, w, h)`: Use this to draw circles (where w = h). **There is no drawCircle() method.**
* **Event Handling:**
    * Interface: `ActionListener`.
    * Method: `public void actionPerformed(ActionEvent e)`.
    * Setup: `myButton.addActionListener(this);`.

---

## 6. Input/Output (I/O)
* **Serialization:**
    * Used to save an object's state to a file.
    * Class must implement `Serializable`.
    * **Write:** `ObjectOutputStream.writeObject()`.
    * **Read:** `ObjectInputStream.readObject()` (Requires casting).
* **Text I/O:**
    * **Write:** `PrintWriter` or `BufferedWriter`.
    * **Read:** `Scanner` or `BufferedReader`.

```java
// Serialization Example
// Writing
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"));
oos.writeObject(myObject);
oos.close();

// Reading
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("data.ser"));
MyClass myObject = (MyClass) ois.readObject();
ois.close();
```

---

## 7. Essential Code Snippets to Memorize

### The "Paint" Pattern
```java
public class MyCanvas extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g); // Important!
        g.setColor(Color.RED);
        g.fillOval(10, 10, 50, 50); // x, y, width, height
    }
}
````

### The "Listener" Pattern

```java
public class MyFrame extends JFrame implements ActionListener {
    JButton btn = new JButton("Click Me");

    public MyFrame() {
        btn.addActionListener(this); // Register listener
        add(btn);
    }

    public void actionPerformed(ActionEvent e) {
        // Handle click
        System.out.println("Button Clicked");
        repaint(); // If visual state changed
    }
}
```

### The "File Write" Pattern

```java
try {
    PrintWriter writer = new PrintWriter(new FileWriter("output.txt"));
    writer.println("Hello World");
    writer.close();
} catch (IOException e) {
    e.printStackTrace();
}
```
### Random Numbers

```java
// Method 1: Math.random() - returns double [0.0, 1.0)
int randomNum = (int)(Math.random() * 100); // 0 to 99

// Method 2: Random class (java.util.Random)
Random rand = new Random();
int randomInt = rand.nextInt(100); // 0 to 99
int randomInRange = rand.nextInt(50) + 1; // 1 to 50
```

### ArrayList Basic Operations

```java
ArrayList<String> list = new ArrayList<>();
list.add("Hello"); // Add element
String item = list.get(0); // Get element at index 0
list.set(0, "World"); // Update element at index 0
list.remove(0); // Remove element at index 0
int size = list.size(); // Get size of the list
```

### Commonly Used Methods

- `isEmpty()`: Check if the list is empty
- `instanceof`: Check object type
- `toString()`: Convert object to string representation
- `double.parseDouble(String s)`: Convert string to double
- `Integer.parseInt(String s)`: Convert string to integer

### String Parsing

- Split a string by spaces
```java
String[] parts = str.split(" ");
```
- Convert string to integer
```java
int num = Integer.parseInt(str);
```
- Convert string to double
```java
double val = Double.parseDouble(str);
```

- Convert integer to string
```java
String str = Integer.toString(num);
```

### Common Exceptions to Remember
- `NullPointerException`: Accessing a null reference.
- `ArrayIndexOutOfBoundsException`: Accessing an invalid array index.
- `ClassCastException`: Invalid type casting.
