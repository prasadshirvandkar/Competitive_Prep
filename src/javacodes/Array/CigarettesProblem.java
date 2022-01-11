package javacodes.Array;

import java.util.ArrayList;
import java.util.List;

public class CigarettesProblem {

    class City {

    }

    final class Person {
        private String name;
        private List<City> city;

        Person(String name, List<City> city) {
            this.name = name;
            this.city = city;
        }

        String getName() {
            return name;
        }

        List<City> getCity() {
            List<City> city1 = new ArrayList<>(city);
            return city1;
        }
    }

    public static void main(String args[]) {
        List<String> persons = new ArrayList<>();

        //Person p1 = new Person("asdasd", new ArrayList<City>());
        
    }
}