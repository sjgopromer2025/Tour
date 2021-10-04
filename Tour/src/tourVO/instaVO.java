package tourVO;

public class instaVO 
{
	private String w_no; 
	private String w_place;
	private String w_pic_0;
	private String w_pic_1;
	private String w_sep; 	
	private String w_insP;
	
	private String i_word;
	private String i_fre;
	
	
	
	
	public String getI_word() {		return i_word;	}
	public void setI_word(String i_word) {		this.i_word = i_word;	}
	public String getI_fre() {		return i_fre;	}
	public void setI_fre(String i_fre) {		this.i_fre = i_fre;	}
	//insP가 0이면 태그 클라우드 1이면 장소 클라우드 이미지
	public String getW_no() 				{	return w_no;			}
	public void setW_no(String w_no) 		{	this.w_no = w_no;		}
	
	public String getW_place()			 	{	return w_place;			}
	public void setW_place(String w_place) 	{	this.w_place = w_place;	}
	
	public String getW_sep() 				{	return w_sep;			}
	public void setW_sep(String w_sep) 		{	this.w_sep = w_sep;		}
	
	public String getW_pic_0() 				{		return w_pic_0;	}
	public void setW_pic_0(String w_pic_0) 	{		this.w_pic_0 = w_pic_0;	}
	public String getW_pic_1() 				{		return w_pic_1;	}
	public void setW_pic_1(String w_pic_1) 	{		this.w_pic_1 = w_pic_1;	}
	public String getW_insP() 				{		return w_insP;	}
	public void setW_insP(String w_insP) 	{		this.w_insP = w_insP;	}
	
	public String getW_insP_path() 			
	{
		String path1 = "../instagram/"+this.w_pic_0;
		String path2 = "../instagram/"+this.w_pic_1;
		return path1+"<<EOF>>"+path2;		
	}
	
	
}
