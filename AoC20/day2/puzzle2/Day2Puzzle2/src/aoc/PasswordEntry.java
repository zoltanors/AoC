package aoc;

public class PasswordEntry {
    private int pos1;
    private int pos2;
    private char c;
    private String pwd;
    private boolean isValid;

    public PasswordEntry(final String line) {
        final String[] fields = line.split("[-: ]");
        pos1 = Integer.valueOf(fields[0]) - 1;
        pos2 = Integer.valueOf(fields[1]) - 1;
        c = fields[2].charAt(0);
        pwd = fields[4];

        char pos1c = pwd.charAt(pos1);
        char pos2c = pwd.charAt(pos2);
        isValid = pos1c == c && pos2c != c ||
            pos1c != c && pos2c == c;
    }

    public boolean isPwdValid() {
        return isValid;
    }

}
