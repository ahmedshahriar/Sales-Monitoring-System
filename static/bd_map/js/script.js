 $(document).ready(function () {
        /* pop up body */
        $description = $(".description");

        /* pop up body on hover effect*/

        $('.enabled').hover(function () {
            console.log($(this).attr("income"));
            /* income for three months (x,y,z) split them intro array */
            $inc = $(this).attr("income").slice(1, -1).split(',');

            /* income for three months assigned in different variables */
            $m1_inc = parseFloat($inc[0]);
            $m2_inc = parseFloat($inc[1]);
            $m3_inc = parseFloat($inc[2]);

            /* N.B : color code - advised not to use hex code */
            $color_code_high_inc = "green";
            $color_code_medium_inc = "Orange";
            $color_code_low_inc = "red";

            /* range 0 - 2k , 2k - 4k , 4k + */
            if ($m1_inc > 0 && $m1_inc < 2000) {
                $first_month_inc_html = "<br><span style='color:" + $color_code_low_inc + ";'>Month 1 : " + $m1_inc + " BDT</span><br>";
                console.log("here 1" + $m1_inc);
            } else if ($m1_inc > 2000 && $m1_inc < 4000) {
                $first_month_inc_html = "<br><span style='color:" + $color_code_medium_inc + ";'>Month 1 : " + $m1_inc + " BDT</span><br>";
                console.log("here 2" + $m1_inc);
            } else {
                $first_month_inc_html = "<br><span style='color:" + $color_code_high_inc + ";'>Month 1 : " + $m1_inc + " BDT</span><br>";
                console.log("here 3" + $m1_inc);
            }

            if ($m2_inc > 0 && $m2_inc < 2000) {
                $second_month_inc_html = "<br><span style='color:" + $color_code_low_inc + ";'>Month 2 : " + $m2_inc + " BDT</span><br>";
                console.log("here 1" + $m2_inc);
            } else if ($m2_inc > 2000 && $m2_inc < 4000) {
                $second_month_inc_html = "<br><span style='color:" + $color_code_medium_inc + ";'>Month 2 : " + $m2_inc + " BDT</span><br>";
                console.log("here 2" + $m2_inc);
            } else {
                $second_month_inc_html = "<br><span style='color:" + $color_code_high_inc + ";'>Month 2 : " + $m2_inc + " BDT</span><br>";
                console.log("here 3" + $m2_inc);
            }

            if ($m3_inc > 0 && $m3_inc < 2000) {
                $third_month_inc_html = "<br><span style='color:" + $color_code_low_inc + ";'>Month 3 : " + $m3_inc + " BDT</span><br>";
                console.log("here 1 " + $m3_inc);
            } else if ($m3_inc > 2000 && $m3_inc < 4000) {
                $third_month_inc_html = "<br><span style='color:" + $color_code_medium_inc + ";'>Month 3 : " + $m3_inc + " BDT</span><br>";
                console.log("here 2 " + $m3_inc);
            } else {
                $third_month_inc_html = "<br><span style='color:" + $color_code_high_inc + ";'>Month 3 : " + $m3_inc + " BDT</span><br>";
                console.log("here 3 " + $m3_inc);
            }

            /* display income for different months' in the pop up box  */
            $(this).attr("class", "enabled heyo");
            $description.addClass('active');

            $description.html($(this).attr('id') + $first_month_inc_html + $second_month_inc_html + $third_month_inc_html);

        }, function () {
            $description.removeClass('active');
        });

        $(document).on('mousemove', function (e) {
            /* positioning the pop up box */
            $description.css({
                left: e.pageX,
                top: e.pageY - 70
            });

        });

    });