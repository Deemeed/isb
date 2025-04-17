import java.security.SecureRandom;
import java.io.FileWriter;
import java.io.IOException;

/**
 * Utility class for generating random binary sequences
 */
class RandomSequenceGenerator {

    /**
     * Generates 128-bit random binary sequence
     * @return String of 128 bits (0s and 1s)
     */
    public static String generate128bitSequence() {
        SecureRandom random = new SecureRandom();
        byte[] randomBytes = new byte[16];
        random.nextBytes(randomBytes);

        StringBuilder binarySequence = new StringBuilder();
        for (byte b : randomBytes) {
            String binaryString = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            binarySequence.append(binaryString);
        }

        return binarySequence.toString();
    }

    /**
     * Saves content to a file
     * @param content The content to save
     * @param filename Target filename
     * @throws IOException If file writing fails
     */
    public static void saveToFile(String content, String filename) throws IOException {
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write(content);
        }
    }
}

/**
 * Main class with program entry point
 */
public class Main {
    /**
     * Main method - program entry point
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        final String FILENAME = "java_sequence.txt";

        try {
            String sequence = RandomSequenceGenerator.generate128bitSequence();
            RandomSequenceGenerator.saveToFile(sequence, FILENAME);
            System.out.println("128-bit sequence saved to " + FILENAME);
            System.out.println("Sequence: " + sequence);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }
}