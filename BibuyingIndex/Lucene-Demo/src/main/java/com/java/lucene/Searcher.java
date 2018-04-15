package com.java.lucene;

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

    static String search1="��";

    public void fun2(String x){
        search1=x;
    }

	public static void search(String indexDir,String q)throws Exception{
		Directory dir=FSDirectory.open(Paths.get(indexDir));
		//����������ȡ��
		IndexReader reader=DirectoryReader.open(dir);
		//����������ѯ��
		IndexSearcher is=new IndexSearcher(reader);
		// ��׼�ִ���
		Analyzer analyzer=new StandardAnalyzer(); 
		//��ʼ��ѯ����
		QueryParser parser=new QueryParser("contents", analyzer);
		Query query=parser.parse(q);
		
		long start=System.currentTimeMillis();
		TopDocs hits=is.search(query, 10);
		long end=System.currentTimeMillis();
		System.out.println("ƥ�� "+q+" ���ܹ�����"+(end-start)+"����"+"��ѯ��"+hits.totalHits+"����¼");
		for(ScoreDoc scoreDoc:hits.scoreDocs){
			Document doc=is.doc(scoreDoc.doc);
//			System.out.println(doc.get("contents"));
			System.out.println(doc.get("fileName"));
//			System.out.println(doc.get("song_name"));
//			System.out.println(doc.get("artist_name"));
//			System.out.println(doc.get("song_name"));
		}
		reader.close();
	}
	
	public static void main(String[] args) {
		//�������·��
		String indexDir="C:\\Users\\SuperTayson\\Desktop\\Bibuying\\DataIndex";
		//��ѯ�ֶ�
		String q=search1;
		try {
			search(indexDir,q);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}



}
