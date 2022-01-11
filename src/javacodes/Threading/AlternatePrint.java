package javacodes.Threading;

class Printer extends Thread {
    int a[] = {1, 3, 5};
    int b[] = {2, 4, 6};

    Object lock = null;

    Printer(Object lock) {
        this.lock = lock;
    }

    int i=0,j=0;
    volatile boolean alternate = false;
    @Override
    public void run() {
        while(i<a.length && j<b.length) {
            if(!alternate && Thread.currentThread().getName().equals("a")) {
                synchronized(lock) {
                    System.out.println(Thread.currentThread().getName()+" -> "+a[i]);
                    i++;
                    try {
                        wait();
                    } catch(InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            } 

            if(alternate && Thread.currentThread().getName().equals("b")) {
                synchronized(lock) {
                    System.out.println(Thread.currentThread().getName()+" -> "+b[j]);
                    j++;
                    notify();
                }
            }
            alternate = !alternate;
        }
    }
}

public class AlternatePrint {
    public static void main(String[] args) {
        Object object = new Object();
        Printer printer1 = new Printer(object);
        printer1.setName("a");
        Printer printer2 = new Printer(object);
        printer1.setName("b");

        printer2.start();
        printer1.start();
    }
}