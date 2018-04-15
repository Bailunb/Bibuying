package com.java.lucene;

public class control {
    static String input1;

    public void set(String x){
        input1=x;
        System.out.println("hello World"+input1);
    }
    control(){
    }
    public static void main(String[] args) throws Exception {
        control c1=new control();
        c1.set("杜");
//        Indexer indexer1=new Indexer();
//        indexer1.main(args);
        Searcher searcher1=new Searcher();
        searcher1.fun2(input1);
        searcher1.main(args);

    }
    public void run(){
        Indexer indexer1=new Indexer();
        indexer1.run();
        Searcher searcher1=new Searcher();
        searcher1.fun2(input1);
        searcher1.run();

    }

}
