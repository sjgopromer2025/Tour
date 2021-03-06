package tourDTO;

import tourVO.*;

public class instaDTO extends CommonDTO
{
	private instaVO i_vo ;

	public void setI_vo(instaVO i_vo) {		this.i_vo = i_vo;	}
	
	public boolean load_w_pic_0()
	{
		try
		{
			this.OpenDB();
			
			String sql = "select w_pic ";
			sql += "from word ";
			sql += "where w_place = '" + this.i_vo.getW_place() + "' ";
			sql += "and w_insP = "+ 0 + " ";
			
			this.RunQuery(sql);
			if(this.GetNextResult() == true)
			{
				this.i_vo.setW_pic_0(this.GetValue("w_pic"));
			}
			
			
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) 
		{
			e.printStackTrace();
			return false;
		}
		
		return true;
	}
	
	public boolean load_w_pic_1()
	{
		try
		{
			this.OpenDB();
			
			String sql = "select w_pic ";
			sql += "from word ";
			sql += "where w_place = '" + this.i_vo.getW_place() + "' ";
			sql += "and w_insP = "+ 1 + " ";
			
			this.RunQuery(sql);
			if(this.GetNextResult() == true)
			{
				this.i_vo.setW_pic_1(this.GetValue("w_pic"));
			}
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) 
		{
			e.printStackTrace();
			return false;
		}
		
		return true;
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
			sql += "where b_sep = 0 and b_place = '"+ this.i_vo.getW_place()+"' ";
			sql += "order by b_fre desc ";
			sql += "limit 0,15 ";
			this.RunQuery(sql);
			String word ="";
			String fre  ="";
			while(this.GetNextResult() == true)
			{
				word += this.GetValue("b_word") + ",";
				fre  += this.GetValue("b_fre")  + ",";
			}
			
			
			this.i_vo.setI_word(word);
			this.i_vo.setI_fre(fre);
			
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
		instaDTO dto = new instaDTO();
		instaVO vo = new instaVO();
		vo.setW_place("????");
		dto.setI_vo(vo);
		dto.load_w_pic_0();
		dto.load_w_pic_1();
		dto.load_graphElement();
		System.out.println(vo.getW_pic_0());
		System.out.println(vo.getW_pic_1());
		System.out.println("=================================");
		String[] word = vo.getI_word().split(",");
		System.out.println(word.length);
		for (int i = 0; i < word.length; i++) {
			System.out.println(i);
			System.out.println(word[i]);
			
		}
		
	}
	

	
	
}
