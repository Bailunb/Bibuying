from jpype import *
import os.path


jvmPath = getDefaultJVMPath()  # the path of jvm.dll

classpath = "/home/supertayson/Desktop/LuceneDemo2.0/Lucene-Demo/target/classes/Lucene-Demo.jar"  # the path of PasswordCipher.class

jvmArg = "-Djava.class.path=" + classpath

if not isJVMStarted():  # test whether the JVM is started

    startJVM(jvmPath, "-ea",jvmArg)  # start JVM
# pkg = JPackage("com.java.lucene")
    javaClass = JClass("com.java.lucene.control")  # create the Java class
    JDClass = JClass("com.java.lucene.a")



try:
    print "1111111111 "
    args=[]
    # jd = javaClass()
    print "333333"
    # javaClass.main()
    # jd.set("x")
    # javaClass.set("x")
    # javaClass.fun11()
    jd = JDClass()
    jd.sayHello("waw")
    print "222222222222222 "

except JavaException, ex:

    print "Caught exception : ", JavaException.message()

    print JavaException.stackTrace()

except:

    print "Unknown Error"

finally:

    shutdownJVM()  # shut down JVM