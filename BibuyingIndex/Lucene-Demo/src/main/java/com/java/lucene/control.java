package com.java.lucene;

public class control {
    static String input1;

    control(String x){
        input1=x;
    }
    public static void main(String[] args) throws Exception {
        control c1=new control("s");
        Indexer indexer1=new Indexer();
        indexer1.main(args);
        Searcher searcher1=new Searcher();
        searcher1.fun2(input1);
        searcher1.main(args);


    }

}
