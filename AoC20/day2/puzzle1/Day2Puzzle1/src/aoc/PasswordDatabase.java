package aoc;

import java.util.ArrayList;
import java.util.List;

public class PasswordDatabase {
    List<PasswordEntry> entries = new ArrayList<PasswordEntry>();

    public int getNoValidPwds() {
        int c = 0;
        for(PasswordEntry e : entries) {
            if (e.isPwdValid()) {
                c++;
            }
        }
        return c;
    }

    public void add(PasswordEntry e) {
        entries.add(e);
    }

}
