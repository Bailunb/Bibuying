package com.java.lucene;

public class control {

    public static void search(String words){
        System.out.println("We are searching for: " + words);
        Searcher s = new Searcher();
        s.run(words);
    }

    public static void main(String[] args) throws Exception {
        //Indexer indexer1 = new Indexer();
        //indexer1.main(args);
        //search("别在夜里等我");
    }
}
