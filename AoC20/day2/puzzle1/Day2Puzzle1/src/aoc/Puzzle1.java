package aoc;

public class Puzzle1 {

	public static void main(String[] args) {
		final Reader reader = new Reader();
		final PasswordDatabase pwdDb = reader.read("Input.txt");
		System.out.println(pwdDb.getNoValidPwds());
	}

}
