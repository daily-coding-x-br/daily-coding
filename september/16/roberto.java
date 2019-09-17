class BitArray {
	byte[] array;
	public BitArray(int size) {
		array = new byte[1 + size/8];
	}
	public void set(int i, int val) {
		int index1 = i/8;
		int index2 = i%8;
		byte b = array[index1];
		byte c = (byte) ((~(1 << index2)) & b);
		array[index1] = (byte) (((1 & val) << index2) | c);
	}
	public int get(int i) {
		int index1 = i/8;
		int index2 = i%8;
		return (array[index1] >> index2) & 1;
	}
}

public class p137 {
	public static void main(String[] args) {
		int size = 9;
		BitArray bitArray = new BitArray(size);

		for (int i=0; i<size; i++) {
			System.out.println(bitArray.get(i));
		}

		for (int i=0; i<size; i++) {
			bitArray.set(i,1);
			System.out.println(bitArray.get(i));
		}

		for (int i=0; i<size; i++) {
			bitArray.set(i,1);
			System.out.println(bitArray.get(i));
		}

		for (int i=0; i<size; i++) {
			bitArray.set(i,0);
			System.out.println(bitArray.get(i));
		}

		for (int i=0; i<size; i++) {
			bitArray.set(i,0);
			System.out.println(bitArray.get(i));
		}
	}
}
