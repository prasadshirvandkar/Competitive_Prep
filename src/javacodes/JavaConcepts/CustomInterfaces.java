package javacodes.JavaConcepts;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ ElementType.CONSTRUCTOR, ElementType.FIELD })
@Retention(RetentionPolicy.RUNTIME)
@interface CustomInt {
    public enum Priority {
        LOW, MEDIUM, HIGH
    }

    Priority setPriority() default Priority.LOW;

    String[] tags() default "";

    boolean isTestable() default false;
}

public class CustomInterfaces {
    public static void main(String[] args) {

    }
}