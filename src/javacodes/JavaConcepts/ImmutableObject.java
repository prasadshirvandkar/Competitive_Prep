package javacodes.JavaConcepts;

class Address {
    private String address;

    Address(String address) {
        this.address = address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getAddress() {
        return this.address;
    }
}

final class Person {
    final private String name;
    final private int age;
    final private Address address;

    Person(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = new Address(address.getAddress());
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public Address getAddress() {
        return new Address(this.address.getAddress());
    }
}

class ImmutableObject {
    public static void main(String[] args) {
        Address address1 = new Address("address1");
        Person person1 = new Person("Prasad", 23, address1);
        Person person2 = person1;
        System.out.println("Person1: "+person1.getAddress().getAddress()+" -> Person2: "+person2.getAddress().getAddress());
        address1.setAddress("addres12312123s");
        System.out.println("Person1: "+person1.getAddress().getAddress()+" -> Person2: "+person2.getAddress().getAddress());

    }
}