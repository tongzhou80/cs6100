import java.nio.file.*;
import java.util.*;

public class MedianAge {
    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get(args[0]));
        List<Integer> ages = new ArrayList<>();

        for (int i = 1; i < lines.size(); i++) {  // skip header
            String[] parts = lines.get(i).split(",");
            ages.add(Integer.parseInt(parts[2]));
        }

        Collections.sort(ages);
        int n = ages.size();
        double median;
        if (n % 2 == 0)
            median = (ages.get(n/2 - 1) + ages.get(n/2)) / 2.0;
        else
            median = ages.get(n/2);

        System.out.println(median);
    }
}
