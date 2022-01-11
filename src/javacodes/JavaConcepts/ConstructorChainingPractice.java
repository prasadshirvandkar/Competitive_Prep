package javacodes.JavaConcepts;

class Base {
    Base() {
        this("Name", 10);
        System.out.println("Base Constructor");
    }

    Base(String name) {
        System.out.println("Base Constructor "+name);
    }

    Base(String name, int value) {
        System.out.println("Base Constructor "+name+ " -> "+value);
    }

    void display() {
        System.out.println("Display Base");
    }
}

class Derived extends Base {

    Derived() {
        super("Dervied");
    }

    Derived(int value) {
        super("Dervied", value);
    }

    Derived(String name, int value) {
        System.out.println("Derived Constructor: "+ name +" -> "+value);
    }

    void display() {
        System.out.println("Display Derived");
    }

}

public class ConstructorChainingPractice {
    public static void main(String[] args) {
        new Base();
        new Base("Base");
        new Base("Base", 20);
        System.out.println(" --------------------------------- ");
        Base b1 = new Derived();
        Base b2 = new Derived(30);
        Derived b3 = new Derived("Derived", 30); 
        b1.display();
        b2.display();
        b3.display();
    }
}