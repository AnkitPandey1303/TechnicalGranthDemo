import streamlit as st

def render():
    st.title("Java Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Java and JVM**
    2. **Basics of Java**: Variables, Data Types, Operators
    3. **Control Flow**: Conditional Statements and Loops
    4. **Functions and Method Overloading**
    5. **Classes, Objects, and Inheritance**
    6. **Interfaces and Abstract Classes**
    7. **Exception Handling in Java**
    8. **File I/O in Java**
    9. **Multithreading Basics**
    10. **Collections Framework**
    """)

    # List of topics and their content
    content = {
        "Introduction to Java and JVM": """
        Java is a popular, object-oriented programming language known for its platform independence. Java code is compiled into bytecode, which is then executed by the Java Virtual Machine (JVM).

        **Key Points:**
        - **Platform Independence**: Java's slogan "Write Once, Run Anywhere" is made possible by the JVM.
        - **JVM**: Java code is compiled into bytecode, and the JVM interprets and runs it on any platform.
        - **Java Development Kit (JDK)**: Includes tools for compiling and running Java applications.

        **Example:**
        ```java
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, Java!");
            }
        }
        ```
        """,

        "Basics of Java: Variables, Data Types, Operators": """
        Java uses variables to store data, and different data types are available for different kinds of information. Operators are used to perform operations on variables.

        **Key Points:**
        - **Variables**: Storage locations with a specific type, e.g., `int x = 5;`
        - **Data Types**: 
            - Primitive types: `int`, `float`, `double`, `char`, `boolean`
            - Reference types: `String`, arrays, and objects
        - **Operators**: Arithmetic (`+`, `-`, `*`), Logical (`&&`, `||`), Comparison (`==`, `!=`, `<`, `>`)
        
        **Example:**
        ```java
        int x = 5;  // Variable assignment
        float y = 10.5f;  // Float data type
        System.out.println(x + y);  // Output: 15.5
        ```
        """,

        "Control Flow: Conditional Statements and Loops": """
        Control flow statements in Java allow decision making and looping.

        **Key Points:**
        - **Conditional Statements**: `if`, `else if`, `else`
        - **Loops**: `for`, `while`, `do-while`
        
        **Example:**
        ```java
        // Conditional statement
        int x = 10;
        if (x > 5) {
            System.out.println("x is greater than 5");
        } else {
            System.out.println("x is less than or equal to 5");
        }

        // For loop example
        for (int i = 0; i < 3; i++) {
            System.out.println(i);  // Output: 0, 1, 2
        }
        ```
        """,

        "Functions and Method Overloading": """
        Functions in Java are reusable blocks of code, and Java supports method overloading, where multiple methods with the same name can exist with different parameters.

        **Key Points:**
        - **Functions**: Defined using `void` or a return type.
        - **Method Overloading**: Defining multiple methods with the same name but different parameters.
        
        **Example:**
        ```java
        public class MathFunctions {
            public int add(int a, int b) {
                return a + b;
            }

            public double add(double a, double b) {
                return a + b;
            }

            public static void main(String[] args) {
                MathFunctions mf = new MathFunctions();
                System.out.println(mf.add(5, 3));  // Output: 8
                System.out.println(mf.add(5.5, 3.5));  // Output: 9.0
            }
        }
        ```
        """,

        "Classes, Objects, and Inheritance": """
        Java is an object-oriented language, and this section covers the fundamental concepts of classes, objects, and inheritance.

        **Key Points:**
        - **Classes**: Blueprints for creating objects.
        - **Objects**: Instances of classes.
        - **Inheritance**: A mechanism to create a new class based on an existing class, inheriting its properties and behaviors.
        
        **Example:**
        ```java
        class Animal {
            void speak() {
                System.out.println("Animal speaks");
            }
        }

        class Dog extends Animal {
            void speak() {
                System.out.println("Dog barks");
            }
        }

        public class Main {
            public static void main(String[] args) {
                Dog dog = new Dog();
                dog.speak();  // Output: Dog barks
            }
        }
        ```
        """,

        "Interfaces and Abstract Classes": """
        Java provides `interfaces` and `abstract classes` to define common behaviors in classes that can be implemented or extended.

        **Key Points:**
        - **Interfaces**: Abstract methods that must be implemented by the classes that implement the interface.
        - **Abstract Classes**: Classes that cannot be instantiated and can have both abstract and concrete methods.
        
        **Example:**
        ```java
        interface Animal {
            void speak();  // Abstract method
        }

        class Dog implements Animal {
            public void speak() {
                System.out.println("Dog barks");
            }
        }

        public class Main {
            public static void main(String[] args) {
                Animal animal = new Dog();
                animal.speak();  // Output: Dog barks
            }
        }
        ```
        """,

        "Exception Handling in Java": """
        Exception handling in Java allows you to handle runtime errors gracefully and provides mechanisms for cleaning up resources after execution.

        **Key Points:**
        - **try-catch**: Used to handle exceptions.
        - **finally**: Used for code that should always run after try-catch blocks.
        
        **Example:**
        ```java
        try {
            int result = 10 / 0;  // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        } finally {
            System.out.println("This will always execute");
        }
        ```
        """,

        "File I/O in Java": """
        Java provides libraries for file handling that allows reading and writing to files.

        **Key Points:**
        - **File Reader/Writer**: Used for reading and writing text files.
        - **BufferedReader/BufferedWriter**: For efficient reading and writing.
        
        **Example:**
        ```java
        import java.io.*;

        public class FileExample {
            public static void main(String[] args) {
                try {
                    BufferedWriter writer = new BufferedWriter(new FileWriter("example.txt"));
                    writer.write("Hello, Java!");
                    writer.close();

                    BufferedReader reader = new BufferedReader(new FileReader("example.txt"));
                    String line = reader.readLine();
                    System.out.println(line);  // Output: Hello, Java!
                    reader.close();
                } catch (IOException e) {
                    System.out.println("An error occurred.");
                }
            }
        }
        ```
        """,

        "Multithreading Basics": """
        Multithreading allows concurrent execution of two or more threads to maximize CPU utilization.

        **Key Points:**
        - **Thread**: Represents a single path of execution.
        - **Runnable Interface**: Used to define a task for a thread.
        
        **Example:**
        ```java
        class MyThread extends Thread {
            public void run() {
                System.out.println("Thread is running");
            }
        }

        public class Main {
            public static void main(String[] args) {
                MyThread thread = new MyThread();
                thread.start();  // Output: Thread is running
            }
        }
        ```
        """,

        "Collections Framework": """
        The Java Collections Framework provides a set of classes and interfaces for storing and manipulating data, such as lists, sets, and maps.

        **Key Points:**
        - **List**: Ordered collection (e.g., `ArrayList`)
        - **Set**: Unordered collection (e.g., `HashSet`)
        - **Map**: Collection of key-value pairs (e.g., `HashMap`)
        
        **Example:**
        ```java
        import java.util.*;

        public class CollectionExample {
            public static void main(String[] args) {
                List<String> list = new ArrayList<>();
                list.add("Java");
                list.add("Python");
                System.out.println(list);  // Output: [Java, Python]

                Set<String> set = new HashSet<>();
                set.add("Apple");
                set.add("Banana");
                System.out.println(set);  // Output: [Apple, Banana]

                Map<String, Integer> map = new HashMap<>();
                map.put("John", 25);
                map.put("Jane", 30);
                System.out.println(map);  // Output: {John=25, Jane=30}
            }
        }
        ```
        """,
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
