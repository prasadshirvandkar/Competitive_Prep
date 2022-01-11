package javacodes.DesignPatterns;

import java.util.HashSet;
import java.util.Set;

class Email {

    String title, recipients, message;

    Email(String recipients, String title, String message) {
        this.recipients = recipients;
        this.title = title;        
        this.message = message;
    }

    String getTitle() {
        return title;
    }

    String getRecipients() {
        return recipients;
    }

    String getMessage() {
        return message;
    }
}

class EmailBuilder {

    Set<String> recipients = new HashSet<>();
    String title;
    String message;
    String closingMessage;
    
    EmailBuilder addRecipient(String recipient) {
        recipients.add(recipient);
        return this;
    }

    EmailBuilder removeRecipient(String recipient) {
        recipients.remove(recipient);
        return this;
    }

    EmailBuilder addTitle(String title) {
        this.title = title;
        return this;
    }

    EmailBuilder addMessage(String message) {
        this.message = message;
        return this;
    }

    EmailBuilder addClosingMessage(String closingMessage) {
        this.closingMessage = closingMessage;
        return this;
    }

    Email build() {
        String concatRecipients = "";
        for(String s: recipients) {
            concatRecipients += s;
        }
        String newMessage = message + "\n\n" + closingMessage;

        return new Email(title, concatRecipients,newMessage);
    }
}


public class BuilderDesign {
    public static void main(String[] args) {
        Email email = new EmailBuilder()
            .addRecipient("shirvandkar.prasad@gmail.com")
            .addTitle("This Title")
            .addMessage("This Message is very Short")
            .addClosingMessage("Thanks and Regards")
            .build();

        System.out.println(email.getMessage());
    }
}