package javacodes.JavaConcepts;

class BasePractice {
    int value = 0;
    BasePractice() { 
        addValue(); 
    }

    void addValue() {
        value += 10;
        System.out.println("Called Base");
    }

    int getValue() { 
        return value;
    }
}

class DerivedPractice extends BasePractice {
    DerivedPractice() { 
        addValue(); 
    }

    void addValue() {
        value += 20;
        System.out.println("Called Derived");
    }
}

public class InheritancePractice {
    public static void main(String[] args) {
        BasePractice b = new DerivedPractice();
        System.out.println(b.getValue());
    }
}