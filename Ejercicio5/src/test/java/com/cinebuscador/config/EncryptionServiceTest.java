
package com.cinebuscador.config;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

public class EncryptionServiceTest {

    private String guardar(String password) throws Exception {
        try {
            return (String) EncryptionService.class
                .getMethod("hashPassword", String.class)
                .invoke(null, password);
        } catch (NoSuchMethodException e) {
            return (String) EncryptionService.class
                .getMethod("encrypt", String.class)
                .invoke(null, password);
        }
    }

    @Test
    void testSaltAleatorio() throws Exception {
        String clave1 = guardar("123456");
        String clave2 = guardar("123456");

        assertNotEquals(clave1, clave2);
    }
}
