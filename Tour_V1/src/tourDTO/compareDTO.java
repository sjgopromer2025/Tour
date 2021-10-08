package tourDTO;

import tourVO.compareVO;

public class compareDTO extends CommonDTO 
{
	private compareVO co_vo ;

	public void setI_vo(compareVO co_vo) {		this.co_vo = co_vo;	}
	
	public boolean loadWord()
	{
		boolean flag = false;
		
		try
		{
			this.OpenDB();
			String sql = "";
			sql += "select co_word2 ";
			sql += "from compare_wd ";
			sql += "where co_place = '"+this.co_vo.getCo_place()+"' ";
			sql += "and co_word1 = '" + this.co_vo.getCo_word1() + "' ";
			sql += "and co_rr > 0.8 and co_idf >= 5 ";
			sql += "order by co_idf desc ";
			sql += "limit 0,15";
			System.out.println(sql);
			String word = "";
			this.RunQuery(sql);
			while(this.GetNextResult() == true)
			{
				if(word.equals(""))
				{
					word += this.GetValue("co_word2");
				}else
				{
					word += ","+this.GetValue("co_word2");
				}
				flag = true;
			}
			
			this.co_vo.setCo_word2(word);
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) {
			e.printStackTrace();
			System.out.println("compareDTO 오류");
			return false;
		}
		return flag;
	}
	
	public static void main(String[] args) 
	{
		compareDTO c = new compareDTO();
		compareVO v = new compareVO();
		
		v.setCo_place("임실");
		v.setCo_word1("운암면");
		
		c.setI_vo(v);
		
		System.out.println(c.loadWord());
		System.out.println(v.getCo_word2());
		
	}
	

}
