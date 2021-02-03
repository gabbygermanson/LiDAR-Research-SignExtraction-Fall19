import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.DecimalFormat;

public class GPStoUTM {

    public static void main(String args[]) {
        String row1;

        try {
            BufferedReader csvReader1 = new BufferedReader(new FileReader("V_20180816_I285_EB_run1(0)_2nd_leg.csv"));
            csvReader1.readLine();

            FileWriter csvWriter = new FileWriter("UTMjava.csv");
            csvWriter.append("Id,Easting,Northing,Retro,Angle,UTC,X,Y,Z,Distance");
            csvWriter.append("\n");

            while ((row1 = csvReader1.readLine()) != null) {
                String[] data1 = row1.split(",");
                csvWriter.append(data1[0]);
                csvWriter.append(",");

                Conversion convert = new Conversion(Double.parseDouble(data1[2]), Double.parseDouble(data1[1]));
                csvWriter.append(String.valueOf(convert.Easting));
                csvWriter.append(",");
                csvWriter.append(String.valueOf(convert.Northing));
                csvWriter.append(",");
                csvWriter.append(data1[6]);
                csvWriter.append(",");
                csvWriter.append(data1[4]);
                csvWriter.append(",");
                csvWriter.append(data1[7]);
                csvWriter.append(",");
                csvWriter.append(data1[1]);
                csvWriter.append(",");
                csvWriter.append(data1[2]);
                csvWriter.append(",");
                csvWriter.append(data1[3]);
                csvWriter.append(",");
                csvWriter.append(data1[5]);
                csvWriter.append("\n");
            }

            csvWriter.flush();
            csvWriter.close();

            try {
                csvReader1.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

        //To test how many lines outputted. Should be 2,000,001
        // try {
        //     BufferedReader csvReader = new BufferedReader(new FileReader("UTMjava.csv"));
        //     int i = 0;
        //     while (csvReader.readLine() != null) {
        //         i++;
        //     }
        //     System.out.println(i);

        //     csvReader.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }



  }