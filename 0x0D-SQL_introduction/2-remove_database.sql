-- This script will delete the database hbtn_0c_0 from a server --
-- hbtn_0c_0 should have root privilege --
IF hbtn_0c_0 IS NOT NULL
	        DELETE DATABASE hbtn_0c_0;
	ELSE
		        RETURN;
