from jpype import getDefaultJVMPath
from jpype import isJVMStarted
from jpype import startJVM
from jpype import JClass
from jpype import JavaException
from jpype import shutdownJVM
import os.path


def query(words):
    jvmPath = getDefaultJVMPath()  # the path of jvm.dll
    classpath = os.getcwd()+"/BibuyingIndex/" + "/Lucene-Demo/classes/artifacts/Lucene_Demo_jar/Lucene-Demo.jar"
    print(classpath)
    jvmArg = "-Djava.class.path=" + classpath
    if not isJVMStarted():
        startJVM(jvmPath, "-ea", jvmArg)
    javaClass = JClass("com.java.lucene.control")  # error
    print(words)
    try:
        # change this to file operations
        javaClass.search(words)
    except JavaException as e:
        print("Caught exception : ", JavaException.message())
        print(JavaException.stackTrace())
    # shutdownJVM()  # danger


if __name__ == '__main__':
    # query("别在夜里等我")
    # query("别在夜里等我")
    pass
