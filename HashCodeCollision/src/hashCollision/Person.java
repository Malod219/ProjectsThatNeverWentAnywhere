package hashCollision;

public class Person {
	private String name;
	private int age;
	
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public int getAge() {
		return age;
	}
	
	public String getName() {
		return name;
	}
	
	public int hashCode() {
		int hc = 17;
		int multiplier = 37;
		
		hc = multiplier * hc + (name == null ? 0 : name.hashCode());
		
		return 37 * hc + age;
	}

}
