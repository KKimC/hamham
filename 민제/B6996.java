package baekjoon;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class B6996 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> output = new ArrayList<>();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int input = Integer.parseInt(br.readLine());

        for (int i = 0; i < input; i++){
            String[] s = br.readLine().split(" ");
            if(s[0].length() != s[1].length()){
                output.add(String.format("%s & %s are NOT anagrams.", s[0], s[1]));
                continue;
            }
            String x = s[0].chars()        // IntStream
                    .sorted()
                    .collect(StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append)
                    .toString();

            String y = s[1].chars()        // IntStream
                    .sorted()
                    .collect(StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append)
                    .toString();

            if (x.equals(y)){
                output.add(String.format("%s & %s are anagrams.", s[0], s[1]));
            }else{
                output.add(String.format("%s & %s are NOT anagrams.", s[0], s[1]));
            }
        }
        for (String s : output){
            bw.write(s);
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
