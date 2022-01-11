package javacodes.JavaConcepts;

class Table {
    static synchronized void printTable(String threadName, int n) {
        for(int i=1;i<3;i++) { System.out.print(threadName+" -> "+(n*i)+" "); }
        try {
            Thread.sleep(300);
        } catch(Exception ignored){}
        System.out.println();
    }

    void printTableTwo(String name) {
        try {
            System.out.println("Print Table Two: "+name);
            Thread.sleep(300);
        } catch(Exception ignored) {}
    }
}

class ThreadOne implements Runnable {
    @Override
    public void run() {
        Table.printTable("ThreadOne", 10);
        new Table().printTableTwo("ThreadOne");
    }
}

class ThreadTwo implements Runnable {
    @Override
    public void run() {
        Table.printTable("ThreadTwo", 20);
        new Table().printTableTwo("ThreadTwo");
    }
}

class ThreadThree implements Runnable {
    @Override
    public void run() {
        Table.printTable("ThreadThree", 30);
        new Table().printTableTwo("ThreadThree");
    }
}

class ThreadFour implements Runnable {
    @Override
    public void run() {
        Table.printTable("ThreadFour", 40);
        new Table().printTableTwo("ThreadFour");
    }
}

public class StaticSynchronisedPractice {
    public static void main(String[] args) {
        Thread t1 = new Thread(new ThreadOne());
        t1.start();

        Thread t2 = new Thread(new ThreadTwo());
        t2.start();
        
        Thread t3 = new Thread(new ThreadThree());
        t3.start();

        Thread t4 = new Thread(new ThreadFour());
        t4.start();
    }
}