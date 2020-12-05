package aoc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Reader {

    public PasswordDatabase read(final String filename) {
        final PasswordDatabase db = new PasswordDatabase();

        try {
            final InputStream stream = getClass().getResourceAsStream("/" + filename);
            final InputStreamReader sr = new InputStreamReader(stream);
            final BufferedReader reader = new BufferedReader(sr);
            String line = reader.readLine();
            while (line != null) {
                db.add(new PasswordEntry(line));
                line = reader.readLine();
            }
            reader.close();
            sr.close();
            stream.close();
        } catch (final IOException e) {
            e.printStackTrace();
        }

        return db;
    }

}
