package javacodes.JavaConcepts;

import java.util.concurrent.*;

class Producer extends Thread {
    @Override
    public void run() {
        for(int i=0;i<5;i++) {
            System.out.println("Producing Thread: "+i);
            Thread.yield();
        }
    }
}

class Consumer extends Thread {
    @Override
    public void run() {
        for(int i=0;i<5;i++) {
            System.out.println("Consuming Thread: "+i);
            Thread.yield();
        }
    }
}

class TaskSample implements Runnable {
    private String name;

    public TaskSample(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void run() {
        try {
            Long duration = (long) (Math.random() * 10);
            System.out.println("Executing : " + name+ " -> "+Thread.currentThread().getName());
            TimeUnit.SECONDS.sleep(duration);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class ThreadYield {
    public static void main(String[] args) {
        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(2);
         
        for (int i = 1; i <= 5; i++) {
            TaskSample task = new TaskSample("Task " + i);
            System.out.println("Created : " + task.getName());
 
            executor.execute(task);
        }
        executor.shutdown();
    }
}