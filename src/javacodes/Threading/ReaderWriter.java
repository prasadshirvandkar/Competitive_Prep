package javacodes.Threading;

class ReaderWriter {

    static Semaphore wrt = new Semaphore(1);
    static Semaphore read = new Semaphore(10);
    static int readCount = 0;
    static void write() throws InterruptedException {
        do {
            wrt.acquire();
            System.out.println("Writing...");
            wrt.release();
        } while(true);
    }

    static void read()  throws InterruptedException {
        do {
            read.acquire();
            readCount++;
            if(readCount == 1) wrt.acquire();
            read.release();

            System.out.println("Reading...");
            
            read.acquire();
            readCount--;

            if(readCount == 0) wrt.release();;

            read.release();
        } while(true);
    }
}

class Semaphore {
    volatile int count = 0;
    Semaphore(int count) {
        this.count = count;
    }

    public synchronized void acquire() throws InterruptedException {
        /* if(count > 0) count--;
        else {
            synchronized(this) {
                this.wait();
                count--;
            }
        } */
        while(this.count == 0) wait();
        count--;
    }

    public synchronized void release() { 
        /* count++;
        if(count > 0) {
            this.notify();
        } */
        this.count++;
        this.notify();
    }
}
