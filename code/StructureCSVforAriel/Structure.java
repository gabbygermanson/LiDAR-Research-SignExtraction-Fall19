import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.ArrayList;
import java.text.DecimalFormat;
import java.util.Collections;
import java.util.Map;

public class Structure {

    public static void main(String args[]) {
        String row;
        try {
            BufferedReader csvReader = new BufferedReader(new FileReader("historical-2.csv"));
            csvReader.readLine();

            HashMap<String, HashMap<String, ArrayList<Double>>> ans = new HashMap<>();

            while ((row = csvReader.readLine()) != null) {
                String[] data = row.split(",");

                String signID = data[0];
                // System.out.println(signID);

                Double retro = Double.valueOf(data[4]);
                DecimalFormat df = new DecimalFormat(".###");
                retro = Double.valueOf(df.format(retro));
                // System.out.println(retro);

                String year = data[14].substring(2, 6);
                // System.out.println(year);

                if (!(ans.containsKey(signID))) {
                    HashMap<String, ArrayList<Double>> years = new HashMap<>();
                    ArrayList<Double> myArray = new ArrayList<>();
                    myArray.add(retro);
                    years.put(year, myArray);
                    ans.put(signID, years);
                } else {
                    if (!(ans.get(signID).containsKey(year))) {
                        ArrayList<Double> newArray = new ArrayList<>();
                        newArray.add(retro);
                        ans.get(signID).put(year, newArray);
                    } else {
                        ans.get(signID).get(year).add(retro);
                    }
                }
            }
            try {
                csvReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

            ans.entrySet().forEach(entry -> {
                    entry.getValue().entrySet().forEach(entry1 -> {
                        ArrayList<Double> sortedRetros = entry1.getValue();
                        Collections.sort(sortedRetros);

                        int n = sortedRetros.size();
                        double twentyfifth;
                        double median;
                        double seventyfifth;
                        double standDev;

                        DecimalFormat df1 = new DecimalFormat(".###");
                        twentyfifth = percentiles(sortedRetros, .25, n);
                        twentyfifth = Double.valueOf(df1.format(twentyfifth));

                        median = percentiles(sortedRetros, .5, n);
                        median = Double.valueOf(df1.format(median));

                        seventyfifth = percentiles(sortedRetros, .75, n);
                        seventyfifth = Double.valueOf(df1.format(seventyfifth));

                        standDev = calculateSD(sortedRetros, n);
                        standDev = Double.valueOf(df1.format(standDev));

                        ArrayList<Double> finalNums = new ArrayList<>();

                        finalNums.add(twentyfifth);
                        finalNums.add(median);
                        finalNums.add(seventyfifth);
                        finalNums.add(standDev);

                        entry1.setValue(finalNums);

                    });
                });


                FileWriter csvWriter = new FileWriter("historicalNew.csv");
                csvWriter.append("Sign ID");
                csvWriter.append(",");
                csvWriter.append("Year");
                csvWriter.append(",");
                csvWriter.append("Median");
                csvWriter.append(",");
                csvWriter.append("25%");
                csvWriter.append(",");
                csvWriter.append("75%");
                csvWriter.append(",");
                csvWriter.append("StDev");
                csvWriter.append("\n");


                for (Map.Entry<String, HashMap<String, ArrayList<Double>>> entry11 : ans.entrySet()) {
                    csvWriter.append(entry11.getKey());
                    csvWriter.append("\n");
                    for (Map.Entry<String, ArrayList<Double>> entry12 : entry11.getValue().entrySet()) {
                        csvWriter.append(" ,");
                        csvWriter.append(entry12.getKey());
                        csvWriter.append(",");
                        for (double num : entry12.getValue()) {
                            csvWriter.append(Double.toString(num));
                            csvWriter.append(",");
                        }
                        csvWriter.append("\n");

                    }
                }


                csvWriter.flush();
                csvWriter.close();



        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static double percentiles(ArrayList<Double> array, double percent, int n) {
        double value = percent * n;
        if (value - Math.floor(value) != 0.0) {
            int index = (int) Math.ceil(value);
            return array.get(index - 1);
        } else {
            int index = (int) value;
            return (array.get(index - 1) + array.get(index)) / 2.0;
        }
    }

    public static double calculateSD(ArrayList<Double> array, int n)
    {
        double sum = 0.0;
        double standardDeviation = 0.0;
        for (double num : array) {
            sum += num;
        }

        double mean = sum/n;

        for (double num : array) {
            standardDeviation += Math.pow(num - mean, 2);
        }
        return Math.sqrt(standardDeviation/n);
    }

}


