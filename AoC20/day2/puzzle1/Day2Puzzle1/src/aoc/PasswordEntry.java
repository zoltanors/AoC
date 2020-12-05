package aoc;

public class PasswordEntry {
    private int min;
    private int max;
    private char c;
    private String pwd;
    private boolean isValid;

    public PasswordEntry(final String line) {
        final String[] fields = line.split("[-: ]");
        min = Integer.valueOf(fields[0]);
        max = Integer.valueOf(fields[1]);
        c = fields[2].charAt(0);
        pwd = fields[4];

        int count = 0;

        for(int i = 0; i < pwd.length(); i++) {
            if (c == pwd.charAt(i)) {
                count++;
            }
        }

        isValid = min <= count && max >= count;
    }

    public boolean isPwdValid() {
        return isValid;
    }

}
