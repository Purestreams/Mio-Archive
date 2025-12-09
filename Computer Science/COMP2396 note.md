# COMP2396 Note



## Overriding vs Overloading

Overriding: Occurs when a subclass provides a specific implementation for a method already defined in its superclass. The method signature (name and parameters) must be identical. It enables runtime polymorphism.

Overloading: Occurs when multiple methods in the same class have the same name but different parameter lists (different type, number, or order of arguments). It enables compile-time polymorphism.

Differences: Overriding requires inheritance and same signature; Overloading does not require inheritance and requires different signatures.

## Abstract Class vs Interface

Abstract Class: A class declared with abstract that cannot be instantiated. It can contain instance variables, constructors, and concrete methods. Used for "is-a" relationships sharing state and behavior.

Interface: A contract defining a set of methods. Prior to Java 8, it could only contain abstract methods and constants. Used for "can-do" capabilities and decoupling.

Usage: Use Abstract Class when related classes share code and state. Use Interface to define a role/capability across unrelated classes or to support multiple inheritance of type.

