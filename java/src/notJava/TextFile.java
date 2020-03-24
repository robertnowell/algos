package notJava;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;

/**
* Utility class for reading out a text file line by line.
* Provides callers the ability to get an iterator that reads the file line by line.
*/
public class TextFile implements Iterable<String> {

	
	protected String filename;
	// open file for reading, throw error if issue
	// create iterator
	public TextFile(String filePath) throws FileNotFoundException { // please implement this
		this.filename = filePath;
	}

	

	/** Begin reading the file, line by line. The returned Iterator.next() will return a line. */
	@Override
	public Iterator<String> iterator() {
		return new LineIterator();
	}

	private class LineIterator implements Iterator<String>{
		boolean closed = false;
		BufferedReader reader;
		public LineIterator() {
			try {
				this.reader = new BufferedReader(new FileReader(filename));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		@Override
		public boolean hasNext() {
			if (closed) {
				return false;
			}
			try {
				return reader.ready();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return false;
		}

		@Override
		public String next() {
			String line = null;
			try {
				line = reader.readLine();
				if (line == null) {
					this.reader.close();
					this.closed = true;
					this.reader = null;
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return line;
		}
	}

	public static void main(String[] args) {
		try {
			TextFile tf = new TextFile("test.txt");
			for (String line : tf) {
				System.out.println(line);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
}