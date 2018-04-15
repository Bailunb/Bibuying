package com.java.lucene;

import java.io.File;
import java.io.FileReader;
import java.io.Reader;
import java.nio.file.Paths;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

/**
 * ����Lucene��������
 * @author Administrator
 *
 */
public class Indexer {
	// д����ʵ��
	private IndexWriter writer; 
	
	/**
	 * ���췽�� 
	 * ʵ����IndexWriter
	 */
	public Indexer(String indexDir)throws Exception{
		Directory dir=FSDirectory.open(Paths.get(indexDir));
		// ��׼�ִ���
		Analyzer analyzer=new StandardAnalyzer(); 
		IndexWriterConfig iwc=new IndexWriterConfig(analyzer);
		writer=new IndexWriter(dir, iwc);
	}

    public Indexer() {

    }

    /**
	 * �ر�д����
	 * Ҳ��Ҫ�ͷ���Դ
	 * @throws Exception
	 */
	public void close()throws Exception{
		writer.close();
	}
	
	/**
	 * ����ָ��Ŀ¼�������ļ�
	 * dataDir  ��Ҫ����������Ŀ¼
	 */
	public int index(String dataDir)throws Exception{
		//��������Ŀ¼�µ������ļ�
		File []files=new File(dataDir).listFiles();
		for(File f:files){
			indexFile(f);
		}
		//�����������ļ�����
		return writer.numDocs();
	}

	/**
	 * ����ָ���ļ�
	 * @param f
	 */
	private void indexFile(File f) throws Exception{
		System.out.println("�����ļ���"+f.getCanonicalPath());
		//������һ�����������ʱ���������������к���һ��
		//һ�С�һ�У�����һ�о���һ��Document��һ���ĵ����ĵ���������
		Document doc=getDocument(f);
		writer.addDocument(doc);
	}

	/**
	 * ��ȡ�ĵ����ĵ���������ÿ���ֶ�
	 * @param f
	 */
	private Document getDocument(File f)throws Exception {
		Document doc=new Document();
		System.out.println("hre222   ");
//		JSON json2 = net.sf.json.JSONSerializer.toJSON(f);

//		FileReader fr=new FileReader(f);
//		int ch = 0;
//		String f1="";
//		while((ch = fr.read()) != -1){
//			f1+=(char)ch;
//		}

//		System.out.println(f1);
//		System.out.println(f1.indexOf("{"));
//		String  sub=f1.substring(f1.indexOf("{"));
//		JSONObject jso = JSONObject.fromObject(sub);
//		System.out.println("hre111   ");
//		System.out.println("hre   "+jso.getString("song_name"));
//
//		doc.add(new TextField("song_name", jso.getString("song_name"), Field.Store.YES));
//		doc.add(new TextField("artist_name", jso.getString("artist_name"),Field.Store.YES));
//		doc.add(new TextField("song_lyric", jso.getString("song_lyric"),Field.Store.YES));

		FileReader fr=new FileReader(f);

		doc.add(new TextField("contents",new FileReader(f)));
		doc.add(new TextField("fileName", f.getName(),Field.Store.YES));
		//fullPath ����·��
		doc.add(new TextField("fullPath",f.getCanonicalPath(),Field.Store.YES));
		
		return doc;
	}
	/**
	 * ���Դ�������
	 */
	public static void main(String[] args) {
		//�������Ŀ¼
//		String indexDir="E:\\Bibuying";
		String indexDir="C:\\Users\\SuperTayson\\Desktop\\Bibuying\\DataIndex";
		//��ȡ���ݵ�·��
//		String dataDir="E:\\Bibuying\\SongsData";
		String dataDir="C:\\Users\\SuperTayson\\Desktop\\Bibuying\\SongsData";

		Indexer indexer=null;
		int numIndexed=0;
		long start=System.currentTimeMillis();
		try {
			indexer = new Indexer(indexDir);
			numIndexed=indexer.index(dataDir);
		} catch (Exception e) {
			e.printStackTrace();
		}finally{
			try {
				indexer.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		long end=System.currentTimeMillis();
		System.out.println("����������"+numIndexed+" ���ļ� ������"+(end-start)+" ����");
	}
}
