package tourDTO;

import tourVO.*;

public class naverDTO extends CommonDTO
{
	
	private naverVO nav_vo;
	String w_pic;
	
	public void setNav_vo(naverVO nav_vo) {		this.nav_vo = nav_vo;	}

	public String Read(String loc, String nav_week)
	{
		//nav_vo = new naverVO();
		try
		{
			
			this.OpenDB();
			String sql;
			sql = "";
			sql += "select w_pic ";
			sql += "from word ";
			sql += "where w_place='"+loc+"' and w_sep=1 and w_week='"+nav_week+"' ";
			System.out.println(sql);
			
			this.RunQuery(sql);
			
			while(this.GetNextResult() == true)
			{
				//commnetVO를 만든후 세팅하고 naverList에 저장
				//nav_vo.setW_pic(this.GetValue("w_pic"));
				//w_pic = nav_vo.getW_pic();
				w_pic = this.GetValue("w_pic");
			}
			
			
			this.CloseQuery(); 
			this.CloseDB();
		}catch (Exception e) 
		{
			e.printStackTrace();
			return null;
		}
		
		return w_pic;
	}
	
	public boolean load_graphElement()
	{
		
		try
		{
			this.OpenDB();
			
			/*
			 b_word,b_fre, b_sep,b_place,			
			*/
			String sql = "select b_word, b_fre ";
			sql += "from bar ";
			sql += "where b_sep = 1 and b_place = '"+ this.nav_vo.getW_place() +"' and b_week = "+this.nav_vo.getW_week() +" ";
			sql += "order by b_fre desc ";
			sql += "limit 0,15 ";
			
			this.RunQuery(sql);
			String word =""; //키워드
			String fre  =""; //키워드별 빈도수
			while(this.GetNextResult() == true)
			{
				word += this.GetValue("b_word") + ",";
				fre  += this.GetValue("b_fre")  + ",";
			}
			
			this.nav_vo.setN_word(word);
			this.nav_vo.setN_fre(fre);
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) 
		{
			e.printStackTrace();
			return false;
		}
		
		return true;
	}
	
	public static void main(String[] args)
	{
		
		naverDTO nav_dto = new naverDTO();
		naverVO nav_vo = new naverVO();

		nav_vo.setW_place("군산");
		nav_vo.setW_week("1");
		
		nav_dto.setNav_vo(nav_vo);
		
		if(nav_dto.load_graphElement() == true)
		{
			System.out.println(nav_vo.getN_word());
			System.out.println(nav_vo.getN_fre());
		}
		
		
	}
	
	
	
		
	
}
