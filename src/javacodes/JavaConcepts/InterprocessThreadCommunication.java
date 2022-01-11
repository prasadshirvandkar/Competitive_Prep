package javacodes.JavaConcepts;

import java.util.LinkedList;
import java.util.Queue;

class Sender extends Thread {
    private static final int MAX_SIZE = 5;
    Queue<Integer> packets = new LinkedList<>();
    int packetCounter = 1;

    @Override
    public void run() {
        System.out.println("Sending Packets....");
        while(true) {
            try {
                sendPackets();
                if(packetCounter > 5) break;
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private void sendPackets() throws InterruptedException {
        synchronized (this) {
            while(packets.size() == MAX_SIZE) {
                wait();
            }

            packets.add(packetCounter++);
            notify();
            System.out.println("Sending Packet: "+(packetCounter-1));
        }
    }

    public int receivePackets() throws InterruptedException {
        synchronized (this) {
            notify();
            while (packets.isEmpty()) {
                wait();
            }
            return packets.poll();
        }
    }
}

class Receiver extends Thread {
    Sender sender;
    Receiver(Sender sender) {
        this.sender = sender;
    }

    @Override
    public void run() {
        try {
            System.out.println("Receiving Packets.....");
            while (true) {
                int number = sender.receivePackets();
                System.out.println("Received Packet: "+number);
                if (number > 5) break;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class InterprocessThreadCommunication {
    public static void main(String[] args) {
        Sender sender = new Sender();
        sender.start();
        new Receiver(sender).start();
    }
}
