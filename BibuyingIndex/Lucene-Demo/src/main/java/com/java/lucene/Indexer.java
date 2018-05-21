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
 * 创建Lucene索引的类
 * @author Administrator
 */
public class Indexer {


	// 写索引实例
	private IndexWriter writer; 
	
	/**
	 * 构造方法 
	 * 实例化IndexWriter
	 */
	public Indexer(String indexDir)throws Exception{
		Directory dir=FSDirectory.open(Paths.get(indexDir));
		// 标准分词器
		Analyzer analyzer=new StandardAnalyzer(); 
		IndexWriterConfig iwc=new IndexWriterConfig(analyzer);
		writer=new IndexWriter(dir, iwc);
	}

    public Indexer() {

    }

    /**
	 * 关闭写索引
	 * 也需要释放资源
	 * @throws Exception
	 */
	public void close()throws Exception{
		writer.close();
	}
	
	/**
	 * 索引指定目录的所有文件
	 * dataDir  需要进行索引的目录
	 */
	public int index(String dataDir)throws Exception{
		//遍历索引目录下的所有文件
		File []files=new File(dataDir).listFiles();
		for(File f:files){
			indexFile(f);
		}
		//返回索引的文件数量
		return writer.numDocs();
	}

	/**
	 * 索引指定文件
	 * @param f
	 */
	private void indexFile(File f) throws Exception{
		System.out.println("索引文件："+f.getCanonicalPath());
		//这里有一个概念：索引的时候，它会像数据里行和列一样
		//一行、一行，这里一行就是一个Document，一个文档，文档里又有列
		Document doc=getDocument(f);
		writer.addDocument(doc);
	}

	/**
	 * 获取文档，文档里再设置每个字段
	 * @param f
	 */
	private Document getDocument(File f)throws Exception {
		Document doc=new Document();
		System.out.println("hre222   ");

		FileReader fr=new FileReader(f);

		doc.add(new TextField("contents",new FileReader(f)));
		doc.add(new TextField("fileName", f.getName(),Field.Store.YES));
		//fullPath 完整路径
		doc.add(new TextField("fullPath",f.getCanonicalPath(),Field.Store.YES));
		
		return doc;
	}
	/**
	 * 测试创建索引
	 */
	public static void main(String[] args) {
		String path = System.getProperty("user.dir");
		String indexDir = path + "/DataIndex";
		String dataDir="/home/cww97/文档/Bibuying/SongsData";

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
	public void fun11(){
		System.out.println("33333333333333333333");
	}


	public void run(){
		String path = System.getProperty("user.dir");
		String indexDir = path + "/DataIndex";
		String dataDir="/home/cww97/文档/Bibuying/SongsData";

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
