package hashCollision;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class CollisionFinder {

	public static void main(String[] args) throws IOException {
		// PLAN OF ATTACK
		// First generate all possible hashcodes using 100 common first names, 100 common last names and then ages 1-100(from file and scanner)
		// This should give 100*100*100 different persons so 1 million persons.
		// Loop over all hashcodes and add the hashcode and the person to a map. Hashcode:person key value pairs
		
		FileReader readFirstNames = new FileReader("firstNames.txt");
		FileReader readLastNames = new FileReader("lastNames.txt");
		Scanner sourceFirst = new Scanner(readFirstNames);
		Scanner sourceSecond = new Scanner(readLastNames);
		
		ArrayList<String> fullNames = new ArrayList<String>();
		
		while (sourceFirst.hasNextLine()) {
			String nextLineFirst = sourceFirst.nextLine();
			while (sourceSecond.hasNextLine()) {
				String nextLineSecond = sourceSecond.nextLine();
				fullNames.add(nextLineFirst+" "+nextLineSecond);
			}
			readLastNames = new FileReader("lastNames.txt");
			sourceSecond = new Scanner(readLastNames);
		}
		sourceFirst.close();
		sourceSecond.close();
		readFirstNames.close();
		readLastNames.close();
		//System.out.println(fullNames.size());
		//System.out.println(fullNames.get(5000));
		
		ArrayList<Person> persons = new ArrayList<Person>();
		
		// Loop 100 times to create 100 different persons of differing ages for each of the 10,000 full names to get a total of 1,000,000 persons
		for (String fullName: fullNames) {
			for(int i=1; i <=100; i++) {
				Person person = new Person(fullName, i);
				persons.add(person);
			}
		}
		
		System.out.println(persons.size());
		
		ArrayList<Integer> hashCodes = new ArrayList<>();
		
		for(Person person: persons) {
			int hashCode = person.hashCode();
			if (hashCodes.contains(hashCode)) {
				int index = hashCodes.indexOf(hashCode);
				Person collision1 = persons.get(index);
				Person collision2 = person;
				System.out.println(String.format("Collision between Name:%s,Age%s and\n Name:%s,Age%s", collision1.getName(),collision1.getAge(), collision2.getName(), collision2.getAge()));
			}
			
			hashCodes.add(hashCode); // This is done to keep the total number of elements of hashCodes and persons to add up to the same
		}
	}
	

}
