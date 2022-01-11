package javacodes.CustomImplementations;

interface Log {
    void error(String message);
    void info(String message);
    void warn(String message);
    void debug(String message);
}

class LoggerImpl implements Log {

    @Override
    public void error(String message) {
        System.out.println("Error: "+message);
    }

    @Override
    public void info(String message) {
        System.out.println("Info: "+message);
    }

    @Override
    public void warn(String message) {
        System.out.println("Warn: "+message);
    }

    @Override
    public void debug(String message) {
        System.out.println("Debug: "+message);
    }
}

class Logger {
    private static volatile Log logger = null;

    static Log getInstance(Class className) {
        Log loggerHelper = logger;
        if(loggerHelper == null) {
            synchronized(className) {
                loggerHelper = logger;
                if(loggerHelper == null) {
                    loggerHelper = logger = new LoggerImpl();
                }
            }
        }
        return loggerHelper;
    }

}

class LoggerFactory {
    static Log getInstance(Class className) {
        return Logger.getInstance(className);
    }
}

public class CustomLogging {
    public static void main(String[] args) {
        Log log = LoggerFactory.getInstance(CustomLogging.class);

        log.info("This is an Info Message");
    }
}