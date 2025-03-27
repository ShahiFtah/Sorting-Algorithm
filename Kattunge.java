import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Kattunge {
    public static void main(String[] args) throws FileNotFoundException {

        if( args.length != 1){
            System.out.println("Skriv filnavn og inputfilen");
            return;
        }

        String fil = args[0];

        HashMap<Integer, Integer> parentmap = new HashMap<>();
        //for å lese filen må vi bruke try i tilfelle filen ikke vil åpne eller hvis det oppstår problemer
        try (Scanner scanner = new Scanner(new File(fil))) {

            int Kittennode = scanner.nextInt();
            scanner.nextLine();

            //Les filen linje for linje
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.equals("-1")){
                    break;
                }
            
                String[] linje = line.split( " ");
                int parent = Integer.parseInt(linje[0]);

                for (int i = 1; i < linje.length; i++) {
                    int child = Integer.parseInt(linje[i]);
                    parentmap.put(child, parent);
                }
            }

            //Vi må lagre stien til kattungen, dette gjør vi ved å bruke en arraylist:
            ArrayList<Integer> path = new ArrayList<>();
            int naanode = Kittennode;

            while(parentmap.containsKey(naanode)){
                path.add(naanode);
                naanode = parentmap.get(naanode);
            }

            path.add(naanode);

            for(int node: path){
                System.out.print(node + " ");
            }
            System.out.println("");
        
        }catch (FileNotFoundException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}
    

