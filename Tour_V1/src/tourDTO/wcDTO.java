package tourDTO;
import java.util.ArrayList;

import tourVO.wcVO;


public class wcDTO extends CommonDTO

{
	public wcVO Read(String place)
	{
		wcVO wc = new wcVO();
		
		try 
		{
			this.OpenDB();
			String sql= "";
			sql += "select * ";
			sql += "from wc ";
			sql += "where wc_place='"+ place +"' ";
			System.out.println(sql);
			
			this.RunQuery(sql);
			
			if(this.GetNextResult() == true)
			{
				wc.setWc_no(this.GetValue("wc_no"));
				wc.setWc_local(this.GetValue("wc_local"));
				wc.setWc_place(this.GetValue("wc_place"));
				wc.setWc_location(this.GetValue("wc_location"));
				wc.setWc_explain(this.GetValue("wc_explain"));
				wc.setWc_relate(this.GetValue("wc_relate"));

			}
			this.CloseQuery();
			this.CloseDB();	
		}catch(Exception e)
		{
			return null;
		}
		
		
		return wc;
	}
	
	
	public String load_name()
	{
		String data = "";
		try
		{
			this.OpenDB();
			String sql= "";
			sql += "select wc_place ";
			sql += "from wc ";
			
			this.RunQuery(sql);
			
			while(this.GetNextResult() == true)
			{
				data += this.GetValue("wc_place")+",";
			}
			
			
		}catch(Exception e)
		{
			e.printStackTrace();
			return null;
		}
		
		return data;
	}
	
	public static void main(String[] args)
	{
		
	
//		wcVO wc = dto.Read("????????");
//		System.out.println(wc.getWc_location());
//		System.out.println(wc.getWc_place());
//		System.out.println(wc.getWc_explain());
//		System.out.println(wc.getWc_relate());
//		System.out.println(wc.getWc_local());
		
		
		wcDTO dto = new wcDTO();
		String pl = dto.load_name();
		System.out.println(pl);
	}
 		
	
}
