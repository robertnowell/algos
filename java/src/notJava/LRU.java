package notJava;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class LRU<K, V> {
	LinkedList<Node> l;
	Map ds;
	Map<K, Node> hm;
	int maxSize;
	/**
	 * datasource
	 * map
	 * doubly linked list
	 * size
	 * 
	 * 
	 * methods
	 * 	ctor
	 * 	get
	 */
	public static void main(String[] args) {
		HashMap<String, Integer> m = new HashMap<String, Integer>();
		for (int i = 0; i < 10; i++) {
			m.put(Integer.toString(i), i);
		}
		LRU<String, Integer> lru = new LRU<String, Integer>(m, 5);
		for (int i = 0; i < 10; i++) {
			int val = lru.get(Integer.toString(i));
			System.out.println(val);
			System.out.println(lru);
		}
		String k = Integer.toString(6);
		int val = lru.get(k);
		System.out.println(val);
		System.out.println(lru);
		k = Integer.toString(7);
		val = lru.get(k);
		System.out.println(val);
		System.out.println(lru);
		k = Integer.toString(2);
		val = lru.get(k);
		System.out.println(val);
		System.out.println(lru);
		k = Integer.toString(0);
		val = lru.get(k);
		System.out.println(val);
		System.out.println(lru);
		k = Integer.toString(9);
		val = lru.get(k);
		System.out.println(val);
		System.out.println(lru);
	}

	public LRU(Map<K, V> ds, int size) {
		this.ds = ds;
		this.maxSize = size;
		this.l = new LinkedList<Node>();
		this.hm = new HashMap<K, Node>();
	}
	
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		if (l.size() > 0) {
			Node v = l.getFirst();
			
			System.out.println("size");
			System.out.println(l.size());
			while (v != null) {
				System.out.println(v);

				sb.append(Integer.toString((int) v.val) + ", ");
				v = v.next;
			}
		}
		return sb.toString();
	}

	public synchronized V get(K key) {
		V val;
		if (hm.containsKey(key)) {
			System.out.println("cache hit");
			Node n = hm.get(key);
			// remove from old spot
			// change next prev pointer
			// change neighbor pointers
			Node prev = n.prev;
			Node next = n.next;
			Node first = null;
			if (l.size() > 0) {
				first = l.getFirst();
				first.setPrev(n);
			}
			if (first != n) {
				l.addFirst(n);
				n.setNext(first);
				n.setPrev(null);
			}
			if (prev != null) {
				prev.setNext(next);
			}
			if (next != null) {
				next.setPrev(prev);
			}
			l.removeLastOccurrence(n);
			val = n.val;
		} else {
			val = (V) ds.get(key);
			Node n = new Node(key, val);
			hm.put(key, n);
			Node first = null;
			if (l.size() > 0) {
				first = l.getFirst();
				first.setPrev(n);
			}
			l.addFirst(n);
			n.setNext(first);
		}

//		System.out.println("size");
//		System.out.println(l.size());
//		System.out.println("maxsize");
//		System.out.println(maxSize);
		if (l.size() > maxSize) {
			Node last = l.removeLast();
			hm.remove(last.key);
			if (last.prev != null) {
				last.prev.setNext(null);
			}
		}
		return val;
	}

	class Node{
		public K key;
		public V val;
		Node next = null;
		Node prev = null;
		/*
		 * setnext
		 * setprev
		 * ctor
		 * compare
		 */
		public Node(K key, V val) {
			this.key = key;
			this.val = val;
		}
		public void setNext(Node n) {
			this.next = n;
		}
		public void setPrev(Node n) {
			this.prev = n;
		}
		@Override
		public String toString() {
			String n = (next == null ? "null" : Integer.toString((int) next.val));
			String p =prev == null ? "null" : Integer.toString((int) prev.val);
			String keys = "Node [key=" + (String) key + ", ";
			String vals = "val=" + Integer.toString((int) val) + ", ";
			return keys + vals + "next=" + n  + ", prev=" + p + "]";
		}
		
	}
}
