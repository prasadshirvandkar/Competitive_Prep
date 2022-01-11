package javacodes.JavaConcepts;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Employee {
    private final int id;
    private final String name;
    private final String designation;
    private final boolean isActive;
    private final int salary;

    public Employee(int id, String name, String designation, boolean isActive, int salary) {
        this.id = id;
        this.name = name;
        this.designation = designation;
        this.isActive = isActive;
        this.salary = salary;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getDesignation() {
        return designation;
    }

    public boolean isActive() {
        return isActive;
    }

    public int getSalary() {
        return salary;
    }
}

public class Java8Streams {
    public static void main(String[] args) {
        Employee e1 = new Employee(1, "Prasad", "Developer", true, 64000);
        Employee e2 = new Employee(2, "Shalaka", "Developer", true, 66000);
        Employee e3 = new Employee(3, "Sunil", "AVP", true, 140000);
        Employee e4 = new Employee(4, "Sanjay", "VP", true, 170000);
        Employee e5 = new Employee(5, "kwkqjweb", "ASnasd", false, 124625);
        Employee e6 = new Employee(6, "asgwr3wfsf", "3qsdgsdg", false, 46231);
        Employee e7 = new Employee(7, "qwdqfafs", "dgasr3f", false, 94752);

        List<Employee> employees = new ArrayList<>();
        employees.add(e1); employees.add(e2); employees.add(e3); employees.add(e4);
        employees.add(e5); employees.add(e6); employees.add(e7);

        Map<String, List<Employee>> employeeMap = employees.stream().filter(Employee::isActive)
                .sorted(Comparator.comparingInt(Employee::getSalary).reversed())
                .limit(4)
                .collect(Collectors.groupingBy(Employee::getDesignation));

        int sumTerminal = employees.stream().filter(Employee::isActive)
            .mapToInt(Employee::getSalary)
            .sum();

        System.out.println("Sum: "+sumTerminal);

        for(Map.Entry<String, List<Employee>> entry: employeeMap.entrySet()) {
            System.out.println(entry.getKey());
            for(Employee employee: entry.getValue()) {
                System.out.println("   -"+employee.getName()+" ("+employee.getSalary()+")");
            }
        }

        List<Integer> ints = new ArrayList<>();
        ints.add(1);
        ints.add(2);
        ints.add(3);

        System.out.println(ints.stream().reduce(Integer::sum));

        List<String> strings = new ArrayList<>();
        strings.add("prasadshirvandkar@gmail.com");
        strings.add("prasadshirvandkar1996@gmail.com");
        strings.add("shirvandkar.prasad@gmail.com");
        strings.add("prasadshirvandkar@hotmail.com");
        strings.add("pshirvandkar@yahoo.com");
        strings.add("prasad.shirvandkar@barclays.com");

        boolean areAllGmailAccounts = strings.stream().allMatch(it -> it.contains("shirvandkar"));
        boolean areAnyGmailAccounts = strings.stream().anyMatch(it -> it.endsWith("linked.com"));
        boolean areThereLinkedInAccounts = strings.stream().noneMatch(it -> it.endsWith("linkedin.com"));
        System.out.println(areAllGmailAccounts);
        System.out.println(areAnyGmailAccounts);
        System.out.println(areThereLinkedInAccounts);

        List<String> upperCaseStrings = strings.stream().map(String::toUpperCase).collect(Collectors.toList());
        for(String string: upperCaseStrings) {
            System.out.print(string+" ");
        }

    }
}
