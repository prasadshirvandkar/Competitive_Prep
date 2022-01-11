package javacodes.CustomImplementations;

class Entry<K, V> {
    K key;
    V value;
    int hashValue;
    Entry<K,V> next;

    Entry(K key, V value, int hashValue, Entry<K,V> next) {
        this.key = key;
        this.value = value;
        this.hashValue = hashValue;
        this.next = next;
    }
}

interface MapC<K, V> {
    void put(K key, V value);
    V get(K key);
    void remove(K key);
}

class HashMapC<K, V> implements MapC<K, V> {
    int BUCKET_LENGTH = 16;
    Entry<K,V>[] buckets;
    int currSize = 0;

    HashMapC() {
        buckets = new Entry[BUCKET_LENGTH];
    }

    private boolean isEligibleForRehashing() {
        return currSize >= (BUCKET_LENGTH * 0.75);
    }

    @Override
    public void put(K key, V value) {
        int hashValue = key.hashCode() % BUCKET_LENGTH;
        Entry<K, V> bucketEntry = buckets[hashValue];
        Entry<K, V> entry = new Entry<K,V>(key, value, hashValue, null);
        
        if(bucketEntry != null) {
            while(bucketEntry != null) {
                if(bucketEntry.hashValue == hashValue && bucketEntry.key == key) {
                    bucketEntry.value = value;
                    break;
                }
                bucketEntry = bucketEntry.next;
            }

            if(bucketEntry == null || bucketEntry.next == null) {
                bucketEntry.next = entry;
            }
        } else {
            buckets[hashValue] = entry;
            currSize++;
        }
        
        if(isEligibleForRehashing()) {

        }
    }

    @Override
    public V get(K key) {
        int hashValue = key.hashCode() % BUCKET_LENGTH;
        Entry<K, V> entry = buckets[hashValue];
        if(entry != null) {
            while(entry != null) {
                if(entry.hashValue == hashValue && entry.key == key) {
                    return entry.value;
                }
                entry = entry.next;
            }
        } 

        return null;
    }

    @Override
    public void remove(K key) {
        int hashValue = key.hashCode() % BUCKET_LENGTH;
        Entry<K, V> entry = buckets[hashValue];

        if(entry != null) {
            while(entry.next != null) {
                if(entry.next != null) {
                    if(entry.next.key == key && entry.next.hashValue == hashValue) {
                        entry.next = entry.next.next;
                    }
                }
            }

            if(entry.next != null) {
                if(entry.next.key == key && entry.next.hashValue == hashValue) {
                    entry.next = null;
                }
            }

        }
    }

}

public class CustomHashMap {
    public static void main(String[] args) {
        MapC<Integer, Integer> hashMapC = new HashMapC<>();
        hashMapC.put(1, 10);
        hashMapC.put(2, 20);
        hashMapC.put(3, 30);
        hashMapC.put(1, 90);
        hashMapC.put(3, 100);

        hashMapC.remove(2);

        System.out.println(hashMapC.get(1));
        System.out.println(hashMapC.get(3));
        System.out.println(hashMapC.get(2));
        System.out.println(hashMapC.get(5));
    }
}