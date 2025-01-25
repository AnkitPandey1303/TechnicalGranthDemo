import streamlit as st

def render():
    st.title("C++ Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to C++**
    2. **Variables, Data Types, and Constants**
    3. **Control Structures**: if-else, loops
    4. **Functions in C++**
    5. **Object-Oriented Programming**: Classes and Objects
    6. **Inheritance and Polymorphism**
    7. **Templates and STL (Standard Template Library)**
    8. **Pointers and Memory Management**
    9. **File Handling in C++**
    10. **Exception Handling**
    """)

    # List of topics and their content
    content = {
        "Introduction to C++": """
        C++ is a high-performance, general-purpose programming language. It is widely used for system software, application software, game development, and real-time systems.

        **Key Points:**
        - **Compiled Language**: C++ code is compiled into machine code.
        - **Object-Oriented**: Supports classes, inheritance, polymorphism, etc.
        - **Efficiency**: Known for its ability to provide control over hardware and memory.

        **Example:**
        ```cpp
        #include <iostream>
        using namespace std;

        int main() {
            cout << "Hello, C++!" << endl;
            return 0;
        }
        ```
        """,

        "Variables, Data Types, and Constants": """
        In C++, variables are used to store data. C++ has various data types that can be used to store different kinds of values.

        **Key Points:**
        - **Variables**: Stores values in a program, e.g., `int x = 10;`
        - **Data Types**: 
            - Basic types: `int`, `char`, `float`, `double`, `bool`
            - Complex types: `array`, `struct`, `class`
        - **Constants**: Using `const` to declare constants that can't be changed.

        **Example:**
        ```cpp
        int x = 5; // integer
        const float PI = 3.14; // constant

        cout << "Value of x: " << x << endl;
        cout << "Value of PI: " << PI << endl;
        ```
        """,

        "Control Structures: if-else, loops": """
        C++ provides control structures such as conditional statements and loops to control the flow of execution.

        **Key Points:**
        - **if-else**: Used for decision-making.
        - **Loops**: `for`, `while`, `do-while` for repetitive tasks.

        **Example:**
        ```cpp
        // if-else statement
        int x = 10;
        if (x > 5) {
            cout << "x is greater than 5" << endl;
        } else {
            cout << "x is less than or equal to 5" << endl;
        }

        // For loop example
        for (int i = 0; i < 5; i++) {
            cout << i << " "; // Output: 0 1 2 3 4
        }
        ```
        """,

        "Functions in C++": """
        Functions in C++ allow you to divide the program into smaller, manageable parts. Functions can have parameters and return values.

        **Key Points:**
        - **Function Definition**: `return_type function_name(parameters) {}`.
        - **Function Overloading**: Same function name, different parameters.

        **Example:**
        ```cpp
        // Function to add two numbers
        int add(int a, int b) {
            return a + b;
        }

        int main() {
            cout << add(3, 5) << endl; // Output: 8
            return 0;
        }
        ```
        """,

        "Object-Oriented Programming: Classes and Objects": """
        C++ is an object-oriented language, meaning it uses classes and objects to organize code.

        **Key Points:**
        - **Classes**: Blueprints for creating objects.
        - **Objects**: Instances of classes that hold data and functions.

        **Example:**
        ```cpp
        class Car {
            public:
                string brand;
                string model;
                int year;

                void start() {
                    cout << "Car is starting" << endl;
                }
        };

        int main() {
            Car myCar;
            myCar.brand = "Toyota";
            myCar.model = "Corolla";
            myCar.year = 2020;
            myCar.start();  // Output: Car is starting
            return 0;
        }
        ```
        """,

        "Inheritance and Polymorphism": """
        Inheritance allows one class to inherit properties and behaviors from another class. Polymorphism allows a class to take many forms.

        **Key Points:**
        - **Inheritance**: Enables code reuse, and the derived class inherits the members of the base class.
        - **Polymorphism**: Allows one function or method to behave differently depending on the object.

        **Example:**
        ```cpp
        class Animal {
            public:
                void speak() {
                    cout << "Animal speaks" << endl;
                }
        };

        class Dog : public Animal {
            public:
                void speak() {
                    cout << "Dog barks" << endl;
                }
        };

        int main() {
            Dog dog;
            dog.speak();  // Output: Dog barks
            return 0;
        }
        ```
        """,

        "Templates and STL (Standard Template Library)": """
        Templates allow functions and classes to operate with generic data types. The Standard Template Library (STL) provides common data structures like vectors, maps, etc.

        **Key Points:**
        - **Function Templates**: Allow creating functions that can handle different data types.
        - **STL**: Provides various container classes like `vector`, `map`, and `list`.

        **Example:**
        ```cpp
        template <typename T>
        T add(T a, T b) {
            return a + b;
        }

        int main() {
            cout << add(3, 4) << endl;  // Output: 7
            cout << add(3.5, 4.5) << endl;  // Output: 8
            return 0;
        }
        ```
        """,

        "Pointers and Memory Management": """
        Pointers are variables that store memory addresses. C++ provides direct memory management using pointers.

        **Key Points:**
        - **Pointers**: Used to store the address of another variable.
        - **Memory Management**: Use `new` and `delete` for dynamic memory allocation and deallocation.

        **Example:**
        ```cpp
        int x = 10;
        int *ptr = &x;  // Pointer to x
        cout << *ptr << endl;  // Output: 10

        // Dynamic memory allocation
        int *arr = new int[5];
        arr[0] = 1;
        cout << arr[0] << endl;  // Output: 1
        delete[] arr;
        ```
        """,

        "File Handling in C++": """
        File handling in C++ allows reading from and writing to files using file streams.

        **Key Points:**
        - **ifstream**: Used for input file stream (reading from a file).
        - **ofstream**: Used for output file stream (writing to a file).

        **Example:**
        ```cpp
        #include <fstream>
        using namespace std;

        int main() {
            // Writing to a file
            ofstream outfile("example.txt");
            outfile << "Hello, C++ File Handling!" << endl;
            outfile.close();

            // Reading from a file
            ifstream infile("example.txt");
            string line;
            while (getline(infile, line)) {
                cout << line << endl;  // Output: Hello, C++ File Handling!
            }
            infile.close();
            return 0;
        }
        ```
        """,

        "Exception Handling": """
        C++ provides exception handling to deal with errors during runtime using `try`, `catch`, and `throw`.

        **Key Points:**
        - **try-catch**: Used to handle exceptions that may arise during program execution.
        - **throw**: Used to manually throw an exception.

        **Example:**
        ```cpp
        try {
            int x = 10;
            if (x == 10) {
                throw "Error: x cannot be 10";
            }
        } catch (const char* msg) {
            cout << msg << endl;  // Output: Error: x cannot be 10
        }
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
