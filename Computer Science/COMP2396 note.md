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

```java
// Example of Exception Handling
try {
    // Code that may throw an exception
} catch (IOException e) {
    // Handle IOException
} catch (Exception e) {
    // Handle other exceptions
} finally {
    // Cleanup code (always runs)
}
```

```java
// Example of Throwing an Exception
public void myMethod() throws IOException {
    // Code that may throw IOException
}
```

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


---

## Sample Questions

### 2015 December Q6

#### Question: Briefly explain the major difference between Applet and JApplet?

Answer: Applet: Part of the older AWT (Abstract Window Toolkit). It relies on the operating system's native GUI components (heavyweight).

JApplet: Part of the Swing library. It extends Applet. It supports Swing components (lightweight, pluggable look-and-feel) and has a generic content pane where components must be added (e.g., getContentPane().add()).

#### Question: Draw the layout that will be rendered when the JApplet is initialized in browser.

Answer: The layout consists of a main panel (BoxLayout.Y_AXIS - Vertical) containing an Input Panel (GridLayout 3x2) and other components.

Visual Representation:

```
+-------------------------+
| [ Label A ] [ Text A  ] |  <-- Input Panel (Row 1)
| [ Label B ] [ Text B  ] |  <-- Input Panel (Row 2)
| [ Label C ] [ Text C  ] |  <-- Input Panel (Row 3)
+-------------------------+
|       [ OK Button ]     |  <-- Main Panel adds button below input
+-------------------------+
|        Root 1:          |  <-- Main Panel adds Label R1 below button
+-------------------------+
|        Root 2:          |  <-- Main Panel adds Label R2 below R1
+-------------------------+
```

#### Question: Complete the implementation of the method actionPerformed so that the roots can be calculated and displayed.

Answer:

```Java

public void actionPerformed(ActionEvent e) {
    try {
        // 1. Get input
        double a = Double.parseDouble(text_A.getText());
        double b = Double.parseDouble(text_B.getText());
        double c = Double.parseDouble(text_C.getText());

        // 2. Calculate Determinant (Delta)
        double delta = b * b - 4 * a * c;

        // 3. Calculate Roots
        if (delta >= 0) {
            double r1 = (-b + Math.sqrt(delta)) / (2 * a);
            double r2 = (-b - Math.sqrt(delta)) / (2 * a);
            label_R1.setText("Root 1: " + r1);
            label_R2.setText("Root 2: " + r2);
        } else {
            label_R1.setText("No real roots");
            label_R2.setText("");
        }
    } catch (NumberFormatException ex) {
        label_R1.setText("Invalid Input");
    }
}
```

#### Question: Write the html file for starting this JApplet.

Answer:

```HTML
<html>
<body>
    <applet code="Quadratic.class" width="300" height="300">
    </applet>
</body>
</html>
```


#### Question: Suggest a way for implementing the listeners of more than one button.

Answer: Inside the actionPerformed(ActionEvent e) method, you can check the source of the event using e.getSource() to distinguish between buttons. Example:

```Java
if (e.getSource() == button_OK) {
    // Handle OK
} else if (e.getSource() == button_Cancel) {
    // Handle Cancel
}
```


### 2021 December Section C


Given,
```java
import java.awt.*;
public abstract class Shape {
    protected int centerX, centerY;
    protected int size = 50;
    public abstract void draw(Graphics g);
    public Shape(int centerX, int centerY) {
        this.centerX = centerX;
        this.centerY = centerY;
    }
}

public interface Movable {
    public void moveUp(int amount);
    public void moveDown(int amount);
}
```

**Circle.java Requirements:**

* **Inheritance:** Must be a subclass of `Shape`.
* **Interface:** Must implement the `Movable` interface (added in Task C4).
* **Drawing Logic:** Implement `draw(Graphics g)` to draw a circle centered at `(centerX, centerY)` with a radius equal to the property `size`.
* **Movement Logic:**
    * `moveUp(int amount)`: Move the shape up by the specific amount.
    * `moveDown(int amount)`: Move the shape down by the specific amount.
* **Structure:** Add properties and constructors as needed.

**MyCanvas.java Requirements:**

* **Inheritance:** Must be a subclass of `JPanel`.
* **Method:** Implement `void setShape(Shape shape)` to allow passing a shape object.
* **Painting Logic:** The shape set via `setShape` must be drawn whenever the canvas is painted (inside `paintComponent`).
* **Polymorphism:** Must support drawing any object that inherits from the `Shape` class.

**MyShapeTester.java (Main Program) Requirements:**

* **GUI Setup:**
    * Title: "My Shape Tester".
    * Size: 250 × 250.
    * Close Operation: Program terminates when the window is closed.
    * Layout: Contains two buttons labeled "^" and "v" (small letter 'v').
    * Central Component: An instance of `MyCanvas` must be added to the center.
* **Initialization:** When the program starts, a new `Circle` object must be created and added to the `MyCanvas` object using `setShape()`.
* **Event Handling:**
    * When buttons are clicked, check if the current shape implements `Movable`.
    * "^" Button: Execute `moveUp(10)`.
    * "v" Button: Execute `moveDown(10)`.
    * Repaint: Must call `repaint` after moving.
    * Non-Movable: Do nothing if the shape does not implement `Movable`.

**Answer:**


```java
import java.awt.*;

public class Circle extends Shape implements Movable {

    // Constructor required to match Shape's constructor
    public Circle(int centerX, int centerY) {
        super(centerX, centerY);
    }

    // Task C2: Implement draw method
    @Override
    public void draw(Graphics g) {
        // radius is 'size'. diameter is 'size * 2'.
        // x and y coordinates for fillOval are the top-left corner of the bounding box.
        int x = centerX - size;
        int y = centerY - size;
        int diameter = size * 2;
        
        g.setColor(Color.BLACK); // Screenshot shows a black circle
        g.fillOval(x, y, diameter, diameter);
    }

    // Task C4: Implement Movable interface methods
    @Override
    public void moveUp(int amount) {
        this.centerY -= amount;
    }

    @Override
    public void moveDown(int amount) {
        this.centerY += amount;
    }
}
```

```java
import javax.swing.*;
import java.awt.*;

public class MyCanvas extends JPanel {
    private Shape shape;

    // Task C3: Method to set the shape
    public void setShape(Shape shape) {
        this.shape = shape;
        repaint(); // Ensure it draws immediately when set
    }
    
    // Helper method for Task C5 to access the current shape
    public Shape getShape() {
        return this.shape;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Task C3: Draw the shape if it exists
        if (shape != null) {
            shape.draw(g);
        }
    }
}
```

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyShapeTester extends JFrame {

    private MyCanvas canvas;

    public MyShapeTester() {
        // Task C1: Frame Setup
        setTitle("My Shape Tester");
        setSize(250, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Task C1: Create Buttons
        JButton btnUp = new JButton("^");
        JButton btnDown = new JButton("v"); // Small letter 'v' as requested

        // Task C3: Create Canvas and add to Center
        canvas = new MyCanvas();
        add(btnUp, BorderLayout.NORTH);
        add(canvas, BorderLayout.CENTER);
        add(btnDown, BorderLayout.SOUTH);

        // Task C3: Initialize Circle and add to canvas
        // Placing it roughly in the middle (e.g., 125, 125)
        Circle circle = new Circle(125, 125);
        canvas.setShape(circle);

        // Task C5: Button Event Handling
        ActionListener listener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Shape currentShape = canvas.getShape();

                // Check if the shape implements Movable
                if (currentShape instanceof Movable) {
                    Movable movableShape = (Movable) currentShape;
                    
                    if (e.getSource() == btnUp) {
                        movableShape.moveUp(10);
                    } else if (e.getSource() == btnDown) {
                        movableShape.moveDown(10);
                    }
                    
                    // Repaint after moving
                    canvas.repaint();
                }
            }
        };

        btnUp.addActionListener(listener);
        btnDown.addActionListener(listener);
    }

    public static void main(String[] args) {
        MyShapeTester frame = new MyShapeTester();
        frame.setVisible(true);
    }
}
```