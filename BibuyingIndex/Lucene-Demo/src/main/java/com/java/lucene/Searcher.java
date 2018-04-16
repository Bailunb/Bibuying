package com.java.lucene;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.nio.file.Paths;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

public class Searcher {

	public static void search(String indexDir, String q)throws Exception{
		Directory dir = FSDirectory.open(Paths.get(indexDir));
		IndexReader reader=DirectoryReader.open(dir);
		IndexSearcher is=new IndexSearcher(reader);
		Analyzer analyzer=new StandardAnalyzer();
		QueryParser parser=new QueryParser("contents", analyzer);
		Query query=parser.parse(q);
		
		long start=System.currentTimeMillis();
		TopDocs hits=is.search(query, 10);
		long end=System.currentTimeMillis();
		String out = String.format("Match %s, Time cost: %d ms, Get cnt = %d", q, end-start, hits.totalHits);
		System.out.println(out);
		PrintWriter pw = new PrintWriter(new FileWriter("/home/cww97/文档/Bibuying/BibuyingWeb/static/search_result.txt"));


		for(ScoreDoc scoreDoc:hits.scoreDocs){
			Document doc=is.doc(scoreDoc.doc);
			///home/cww97/文档/Bibuying/BibuyingWeb/static/search_result.txt
			String filename=doc.get("fileName");
			pw.write(filename.substring(0,filename.length()-5));
			pw.write('\n');
			System.out.println(doc.get("fileName"));
		}
		reader.close();
		pw.close();
	}

	public static void run(String words){
		String indexDir = "/home/cww97/文档/Bibuying/BibuyingIndex/Lucene-Demo/DataIndex";
		//System.out.println("fuck ---------> " + indexDir);
		//查询字段
		try {
			search(indexDir, words);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
