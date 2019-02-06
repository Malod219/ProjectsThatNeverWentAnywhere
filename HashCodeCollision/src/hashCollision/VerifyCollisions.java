package hashCollision;

public class VerifyCollisions {

	public static void main(String[] args) {
		//Person person1 = new Person("Austin Collins", 1);
		//Person person2 = new Person("Cameron Brooks", 60);
		Person person1 = new Person("Alex Sanders", 75);
		Person person2 = new Person("Julian Parker", 1);
		// The rest follow logically as it is just addition by 1 for each age, I.E. age 2 matched with age 61
		System.out.println(String.format("Person 1 Hashcode:%s\nPerson 2 Hashcode:%s", person1.hashCode(), person2.hashCode()));

	}

}
