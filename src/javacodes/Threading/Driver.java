package javacodes.Threading;

public class Driver {
    static Object lock = new Object();

    public static void main(String[] args) {
        int a[] = {1, 2, 3};
        int b[] = {4, 5, 6};

        Thread t1 = new Thread(() -> {
            for (int i=0;i<a.length;i++) {
                synchronized (lock) {
                    System.out.println("Even: " + a[i]);
                    try {
                        lock.notify();
                        lock.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i=0;i<b.length;i++) {
                synchronized (lock) {
                    System.out.println("Odd: " + b[i]);
                    try {
                        lock.notify();
                        if(i == b.length - 1) {
                            break;
                        }
                        lock.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });

        t1.start();
        t2.start();
    }
}